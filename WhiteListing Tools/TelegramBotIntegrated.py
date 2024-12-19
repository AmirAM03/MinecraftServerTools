import telebot
import os
import subprocess
import paramiko
import VelocityCoolListPluginWhiteListConvertor

# Add your bot token here
BOT_TOKEN = 'BOT_TOKEN'

# Define a whitelist of chat IDs that are allowed to interact with the bot
ALLOWED_CHAT_IDS = [123456798, 012345678, 987654321]  # Replace with your allowed chat IDs (your allowed staff TLG ids)

# Path where you want to store the file on the Linux server
SERVER_PATH = '/root/ProxyServer/plugins/velocitycoollist/'

# Create the bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Function to save the message content and send it to the server
def save_and_send_file(message):
    chat_id = message.chat.id

    # Check if the chat ID is in the allowed whitelist
    if chat_id not in ALLOWED_CHAT_IDS:
        bot.reply_to(message, "You are not authorized to use this bot.")
        print(f'Not allowed access by {chat_id}')
        return

    # Get the message content
    message_content = message.text

    # Save the content to a file
    filename = f"Temp.txt"
    with open(filename, 'w') as file:
        file.write(message_content)




    # Path to the Python script you want to run
    # script_path = "./VelocityCoolListPluginWhiteListConvertor.py"

    # Run the script using subprocess
    # try:
        # result = subprocess.run(['py', script_path], check=True, capture_output=True, text=True)  # py,python,python3 module is depend to your machine
        # print(f"Script executed successfully: {result.stdout}")
    # except subprocess.CalledProcessError as e:
        # print(f"Script execution failed with error: {e.stderr}")
        
    
    VelocityCoolListPluginWhiteListConvertor.main()


    # Send the file to the server
    send_file_to_server('whitelist.json')

    # Confirm to the user
    bot.reply_to(message, f"Message saved and applied to the server as {filename}, Try to reload vcl whitelist by '/vcl reload'")

    # Clean up the local file
    # os.remove(filename)
    
    
    
    
# Function to send the file to the server using SFTP
def send_file_to_server(local_filename):
    # SSH details of the server
    hostname = 'server_ip'
    port = 22 # Your minecraft server SSH prot
    username = 'ssh_username'
    password = 'ssh_password'  # It's safer to use private key instead of password
    remote_filename = SERVER_PATH + local_filename

    try:
        # Initialize SSH client and connect to the server
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)

        # Use SFTP to transfer the file
        sftp = ssh.open_sftp()
        sftp.put(local_filename, remote_filename)
        sftp.close()

        # Close SSH connection
        ssh.close()

        print(f"File {local_filename} successfully sent to server at {remote_filename}")

    except Exception as e:
        print(f"Failed to send the file: {e}")
    
    
    
    
    
    
# Handler for text messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    save_and_send_file(message)

# Start the bot
bot.polling()