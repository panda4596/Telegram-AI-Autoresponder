import os
import logging
from dotenv import load_dotenv
from telethon import TelegramClient, events
from google import genai

# Load environment variables from .env file
load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini AI Client
ai_client = genai.Client(api_key=GEMINI_KEY)

# Initialize Telethon User Client
client = TelegramClient('my_personal_session', API_ID, API_HASH)

logging.basicConfig(level=logging.INFO)

# Listen for incoming private direct messages (DMs)
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_personal_dm(event):
    sender = await event.get_sender()
    
    # Do not reply if the message is sent by a bot or by the account owner
    if sender.bot or event.out:
        return

    user_message = event.text
    text_lower = user_message.lower().strip()  # Convert message to lowercase for matching
    print(f"New Message: {user_message}")

    try:
        # 1. Attempt to generate a response using Gemini AI
        response = ai_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"You are acting as a polite AI assistant for the account owner's personal Telegram account. Reply briefly and naturally to this message: {user_message}",
        )
        reply_text = response.text if response.text else "Sorry, I couldn't respond right now."
        
        await event.reply(reply_text)
        print(f"Sending Reply (AI): {reply_text}")

    except Exception as e:
        print(f"AI Limit/Error: {e}")
        
        # 2. Rule-based Smart Fallback responses if AI service fails or hits rate limits
        if any(word in text_lower for word in ["hi", "hello", "hey"]):
            fallback_reply = "Hey! The user is currently busy and will get back to you soon."

        elif any(word in text_lower for word in ["how are you"]):
            fallback_reply = "Doing well! How about you? The user will reply once online."

        elif any(word in text_lower for word in ["what are you doing"]):
            fallback_reply = "The user is currently busy with work. They will text you back later!"

        elif any(word in text_lower for word in ["where are you"]):
            fallback_reply = "The user is currently away. Will get in touch with you shortly."

        elif any(word in text_lower for word in ["bye"]):
            fallback_reply = "Goodbye! The user will message or call you as soon as they are free 😊"

        else:
            # Default response for unrecognized queries during fallback
            fallback_reply = "Hey! The user is currently busy or away. They will check your message and reply soon!"

        await event.reply(fallback_reply)
        print(f"Fallback Smart Reply Sent: {fallback_reply}")

print("Successfully activated auto-responder on your personal account..")
client.start()
client.run_until_disconnected()