from bot_config import client, tree, TOKEN
from api_services import generate_discussion_questions
from keep_alive import keep_alive
import discord

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    try:
        await tree.sync()
        print("✅ Slash commands synchronized!")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

@tree.command(name="discuss", description="Generate discussion questions based on group preferences")
async def discuss_command(
    interaction: discord.Interaction,
    duration: int,
    mood: str,
    topics: str,
    question_types: str
):
    if not interaction.user.voice:
        await interaction.response.send_message("You must be in a voice channel to use this command!", ephemeral=True)
        return

    voice_channel = interaction.user.voice.channel
    member_count = len(voice_channel.members)

    await interaction.response.defer()
    topic_list = [t.strip() for t in topics.split(',')]
    question_type_list = [qt.strip() for qt in question_types.split(',')]

    questions = await generate_discussion_questions(
        member_count,
        duration,
        mood,
        topic_list,
        question_type_list
    )

    await interaction.followup.send(
        f"**Discussion Questions Sets for {voice_channel.name}**\n"
        f"Duration: {duration} minutes\n"
        f"Current Mood: {mood}\n"
        f"Topics: {topics}\n"
        f"Question Types: {question_types}\n\n"
        f"Choose a set of questions to discuss:\n\n"
        f"{questions}"
    )

if __name__ == "__main__":
    keep_alive()
    try:
        client.run(TOKEN, reconnect=True)
    except discord.errors.LoginFailure:
        print("ERROR: Invalid Discord token")
    except Exception as e:
        print(f"Error starting bot: {e}")