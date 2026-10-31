prompts = [
    {
        "title": "Python Tutor",
        "category": "Programming",
        "content": "Explain Python concepts with simple examples."
    },
    {
        "title": "AI Research Assistant",
        "category": "AI",
        "content": "Summarize AI research papers in simple language."
    }
]


def find_prompt(title):
    for prompt in prompts:
        if prompt["title"].casefold() == title.casefold():
            return prompt
    return None


def add_prompt():
    print("\n--- Add New Prompt ---")

    title = input("Enter title: ").strip()
    category = input("Enter category: ").strip()
    content = input("Enter prompt content: ").strip()

    if not title or not category or not content:
        print("Error: All fields are required.")
        return

    if find_prompt(title) is not None:
        print("Error: Title already exists.")
        return

    new_prompt = {
        "title": title,
        "category": category,
        "content": content
    }

    prompts.append(new_prompt)
    print("Prompt added successfully!")


def show_prompts():
    print("\n--- Prompt Library ---")

    if not prompts:
        print("No prompts found.")
        return

    for index, prompt in enumerate(prompts, start=1):
        print(f"{index}. {prompt['title']} [{prompt['category']}]")


def search_prompt():
    print("\n--- Search Prompt ---")

    title = input("Enter title to search: ").strip()
    prompt = find_prompt(title)

    if prompt is None:
        print("Prompt not found.")
        return

    print("\nPrompt found!")
    print("Title:", prompt["title"])
    print("Category:", prompt["category"])
    print("Content:", prompt["content"])


def edit_prompt():
    print("\n--- Edit Prompt ---")

    title = input("Enter title to edit: ").strip()
    prompt = find_prompt(title)

    if prompt is None:
        print("Prompt not found.")
        return

    new_title = input(
        f"New title [{prompt['title']}]: "
    ).strip()

    new_category = input(
        f"New category [{prompt['category']}]: "
    ).strip()

    new_content = input(
        "New content (leave blank to keep current): "
    ).strip()

    if new_title:
        existing_prompt = find_prompt(new_title)

        if existing_prompt is not None and existing_prompt is not prompt:
            print("Error: Title already exists.")
            return

        prompt["title"] = new_title

    if new_category:
        prompt["category"] = new_category

    if new_content:
        prompt["content"] = new_content

    print("Prompt updated successfully!")


def delete_prompt():
    print("\n--- Delete Prompt ---")

    title = input("Enter title to delete: ").strip()
    prompt = find_prompt(title)

    if prompt is None:
        print("Prompt not found.")
        return

    confirmation = input(
        f"Delete '{prompt['title']}'? (y/n): "
    ).strip().casefold()

    if confirmation == "y":
        prompts.remove(prompt)
        print("Prompt deleted successfully.")
    else:
        print("Deletion cancelled.")


def main():
    while True:
        print("\n========== PromptVault ==========")
        print("1. Show all prompts")
        print("2. Add a prompt")
        print("3. Search for a prompt")
        print("4. Edit a prompt")
        print("5. Delete a prompt")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_prompts()
        elif choice == "2":
            add_prompt()
        elif choice == "3":
            search_prompt()
        elif choice == "4":
            edit_prompt()
        elif choice == "5":
            delete_prompt()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
