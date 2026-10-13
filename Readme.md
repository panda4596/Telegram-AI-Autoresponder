Telegram AI Auto-Responder

Description

Telegram AI Auto-Responder is a Python project that automatically responds to personal Telegram direct messages when you are busy or away. It uses Telethon for Telegram integration and the Groq API for fast AI text generation, including a free-access option subject to current Groq limits and availability.

Fallback behavior

If the Groq API is unavailable, rate-limited, or otherwise fails, the responder sends a polite rule-based message instead of leaving the conversation unanswered.



Features

Automated personal-DM responses — Responds to incoming personal Telegram direct messages while you are busy or away.

Natural, polite replies — Uses the Groq API to generate concise and context-aware text when the service is available.

Rule-based fallback — Sends a predictable, courteous response when Groq is unavailable, rate-limited, or returns an error.

Configurable busy messaging — Lets you define the tone and wording of your away or busy response.

Secure configuration — Reads credentials from environment variables instead of requiring secrets in source files.

Error handling — Handles API and connection failures without crashing on a single unsuccessful response attempt.

Easy local setup — Uses a standard Python virtual environment and dependency installation workflow.


Prerequisites

Before installing the project, make sure you have the following:

Python 3.9 or newer installed and available on your command line.

A Telegram account that will run the responder.

Telegram API credentials obtained from my.telegram.org, including an API ID and API hash.

A Groq API key created through the Groq developer console.

An internet connection so the application can communicate with Telegram and, when enabled, the Groq API.

Important

The responder requires an authenticated Telegram session and valid credentials for every external service it uses.



Installation Steps

Clone the repository.

git clone <repository-url


Enter the project directory.

cd Telegram-AI-Auto-Responder


Create and activate a virtual environment. Use the commands for your operating system.

macOS or Linux

python3 -m venv .venv 
source .venv/bin/activate


Windows PowerShell

python -m venv .venv 
.venv\Scripts\Activate.ps1


Windows Command Prompt

python -m venv .venv 
.venv\Scripts\activate.bat


Install the project dependencies.

python -m pip install -r requirements.txt


Create the environment file. Create an empty file named .env in the project root.

macOS or Linux

touch .env


Windows PowerShell

New-Item .env -ItemType File


Run the application. If the project uses a different entry-point filename, substitute it for main.py.

python main.py



Environment Variables

Add the following variables to the .env file in the project root.

Variable

Purpose

Where to get it


TELEGRAM_API_ID

Numeric identifier used by Telethon to connect to Telegram.

From the Telegram application details page on my.telegram.org.


TELEGRAM_API_HASH

Secret hash paired with the Telegram API ID.

From the same Telegram application details page on my.telegram.org.


GROQ_API_KEY

Credential used to request AI-generated replies from Groq.

From your Groq account's API key management area.


Safe placeholder example

TELEGRAM_API_ID=your_telegram_api_id 
TELEGRAM_API_HASH=your_telegram_api_hash 
GROQ_API_KEY=your_groq_api_key



Keep credentials private

Never commit .env to version control, publish it in an issue or log, or expose Telegram and Groq credentials in screenshots, code, or public repositories.



Usage

Configure the environment. Add your Telegram API ID, Telegram API hash, and Groq API key to .env using the names documented above.

Start the responder. Activate the virtual environment and run the project's entry point, such as python main.py when that file is provided by the repository.

Complete first-login verification. When Telethon prompts you, enter the phone number, login code, and any two-step verification password requested for the Telegram account.

Keep the process running. Leave the terminal session or hosting process active so the responder can receive and process new personal direct messages.

Test from another Telegram account. Send a direct message to the configured account and confirm that the generated reply or polite fallback is delivered as expected.

Stop safely. Return to the running terminal and press Ctrl+C to request a clean shutdown.

Expected Configuration and Behavior

Example

With valid credentials in .env, the application starts a Telethon session, watches personal direct messages, and uses Groq to generate a natural reply. If Groq cannot be reached or the request is limited, it sends the configured rule-based busy response instead.


Troubleshooting

Issue

What to check


Invalid Telegram credentials

Confirm that TELEGRAM_API_ID is numeric, the API hash is copied exactly, and both values came from the same Telegram application.


Groq limits or downtime

Verify the API key, review the current Groq quota or service status, and confirm that the rule-based fallback still provides an acceptable response.


Telegram session authentication

Complete the first-login code and two-step verification prompts, use the correct phone number, and allow the session file to be created where the application expects it.


No response during testing

Confirm the process is still running, the test is a personal direct message, the internet connection is available, and the terminal shows no configuration or connection error.


Security Notes

Protect API credentials. Store secrets only in environment variables or another secure secret store, and rotate them if they are exposed.

Protect the Telegram session. Treat any Telethon session file as sensitive because it may allow access to the authenticated account.

Limit access. Run the responder on a trusted machine and review generated replies before using it for important conversations.
