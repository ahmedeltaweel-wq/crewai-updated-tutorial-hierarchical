from datetime import datetime


def save_service_report(task_output):
    """Save customer service report"""
    # Get today's date and time
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # Set the filename
    filename = f"service_report_{timestamp}.txt"
    
    # Write the task output to the file
    with open(filename, 'w', encoding='utf-8') as file:
        # Use .raw instead of .result for newer CrewAI versions
        content = str(task_output.raw) if hasattr(task_output, 'raw') else str(task_output)
        file.write(content)
    
    print(f"✅ Service report saved: {filename}")
    return filename
