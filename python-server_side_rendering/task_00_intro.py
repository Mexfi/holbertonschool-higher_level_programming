import os
import sys

# Define the required placeholders to check for missing data
PLACEHOLDERS = ["{name}", "{event_title}", "{event_date}", "{event_location}"]
PLACEHOLDER_KEYS = ["name", "event_title", "event_date", "event_location"]

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template string with placeholders.
        attendees (list): A list of dictionaries, where each dictionary
                          contains data for one attendee.
    """
    
    # Set up basic logging (printing to stderr/stdout for simplicity)
    def log_error(message):
        """Helper function for consistent error logging."""
        sys.stderr.write(f"ERROR: {message}\n")

    # --- 1. Check Input Types ---
    if not isinstance(template, str):
        log_error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list):
        log_error("Invalid input: attendees must be a list.")
        return
    
    # Check if all elements in the list are dictionaries
    if attendees and not all(isinstance(a, dict) for a in attendees):
        log_error("Invalid input: attendees list must contain only dictionaries.")
        return

    # --- 2. Handle Empty Inputs ---
    if not template.strip():
        log_error("Template is empty, no output files generated.")
        return

    if not attendees:
        log_error("No data provided, no output files generated.")
        return

    # --- 3. Process Each Attendee and Generate Output Files ---
    
    for index, attendee in enumerate(attendees):
        output_filename = f"output_{index + 1}.txt"
        
        # Start with the original template for each attendee
        personalized_template = template
        
        # Process placeholders for the current attendee
        for key in PLACEHOLDER_KEYS:
            placeholder = f"{{{key}}}"
            
            # Retrieve value, handling missing key or None value
            value = attendee.get(key)
            
            # --- 4. Missing Data in Object Handling ---
            if value is None or value == "":
                # Replace placeholder with "N/A"
                replacement = "N/A"
            else:
                # Use the provided value, converting to string if necessary
                replacement = str(value)

            # Substitute the placeholder in the template
            personalized_template = personalized_template.replace(placeholder, replacement)
        
        # --- 5. Generate Output Files ---
        try:
            with open(output_filename, 'w') as f:
                f.write(personalized_template)
            # print(f"Successfully generated {output_filename}") # Uncomment for verification
            
        except IOError as e:
            log_error(f"Failed to write file {output_filename}: {e}")
            
# --- Example Usage (Matching the main file to test the program) ---
if __name__ == '__main__':
    # Create the template file content for testing
    TEMPLATE_CONTENT = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
"""
    # Create template.txt for testing the file read operation
    with open('template.txt', 'w') as f:
        f.write(TEMPLATE_CONTENT)

    # List of attendees for testing
    attendees_data = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        # Charlie is missing 'event_date' value (None)
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"},
        # David is missing 'event_title' key completely
        {"name": "David", "event_date": "2023-12-01", "event_location": "Remote"}
    ]

    # --- Test Case: Valid Input ---
    print("--- Running Test Case: Valid Input ---")
    with open('template.txt', 'r') as file:
        template_content = file.read()
    generate_invitations(template_content, attendees_data)
    
    # You can now check for output_1.txt, output_2.txt, output_3.txt, output_4.txt

    # --- Test Case: Empty Attendees List ---
    print("\n--- Running Test Case: Empty Attendees List ---")
    generate_invitations(template_content, []) # Should log: "No data provided..."

    # --- Test Case: Invalid Template Type ---
    print("\n--- Running Test Case: Invalid Template Type ---")
    generate_invitations(123, attendees_data) # Should log: "Invalid input: template must be a string."
    
    # --- Test Case: Invalid Attendees Type ---
    print("\n--- Running Test Case: Invalid Attendees Type ---")
    generate_invitations(template_content, "not a list") # Should log: "Invalid input: attendees must be a list."
    
    # --- Test Case: Invalid Attendees List Content ---
    print("\n--- Running Test Case: Invalid Attendees List Content ---")
    generate_invitations(template_content, [{"name": "A"}, "not a dict"]) # Should log: "Invalid input: attendees list must contain only dictionaries."
    
    # --- Test Case: Empty Template ---
    print("\n--- Running Test Case: Empty Template ---")
    generate_invitations("", attendees_data) # Should log: "Template is empty..."
