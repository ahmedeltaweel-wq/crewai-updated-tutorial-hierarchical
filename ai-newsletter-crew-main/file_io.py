from datetime import datetime


def save_markdown(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"{today_date}.md"
    # Write the task output to the markdown file
    with open(filename, 'w', encoding='utf-8') as file:
        # Use .raw instead of .result for newer CrewAI versions
        content = str(task_output.raw) if hasattr(task_output, 'raw') else str(task_output)
        file.write(content)
    print(f"Newsletter saved as {filename}")
