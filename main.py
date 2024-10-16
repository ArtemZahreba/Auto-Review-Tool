#main.py
import tempfile
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from config import WHITE, GREEN, RESET_COLOR, model_name, OPENAI_API_KEY
from utils import format_user_question
from file_processing import clone_github_repo, load_and_index_files
from questions import ask_question, QuestionContext


def main():
    github_url = input("Enter the GitHub URL of the repository: ")
    repo_name = github_url.split("/")[-1]

    # Додані запити на опис проекту та рівень спеціаліста
    project_description = input("Enter the project description: ")
    specialist_level = input("Enter the specialist level (junior, middle, senior): ")

    print("Cloning the repository...")
    with tempfile.TemporaryDirectory() as local_path:
        if clone_github_repo(github_url, local_path):
            index, documents, file_type_counts, filenames = load_and_index_files(local_path)
            if index is None:
                print("No documents were found to index. Exiting.")
                exit()

            print("Repository cloned. Indexing files...")
            llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.2)

            template = """
            Repo: {repo_name} ({github_url}) | Conv: {conversation_history} | Docs: {numbered_documents} | Q: {question} | FileCount: {file_type_counts} | FileNames: {filenames} | ProjectDescription: {project_description} | SpecialistLevel: {specialist_level}

            Instr:
            1. Evaluate how well the task was completed based on the project description and specialist level.
            2. Provide feedback and assessment.
            3. Focus on repo/code.
            4. Unsure? Say "I am not sure".

            Answer:
            """

            prompt = PromptTemplate(
                template=template,
                input_variables=["repo_name", "github_url", "conversation_history", "question", "numbered_documents",
                                 "file_type_counts", "filenames", "project_description", "specialist_level"]
            )

            llm_chain = LLMChain(prompt=prompt, llm=llm)

            conversation_history = ""
            question_context = QuestionContext(index, documents, llm_chain, model_name, repo_name, github_url,
                                               conversation_history, file_type_counts, filenames)
            while True:
                try:
                    user_question = input(
                        "\n" + WHITE + "Ask a question about the repository (type 'exit()' to quit): " + RESET_COLOR)
                    if user_question.lower() == "exit()":
                        break
                    print('Thinking...')
                    user_question = format_user_question(user_question)

                    # Додаємо опис проекту та рівень спеціаліста до контексту запитання
                    answer = ask_question(user_question, question_context, project_description, specialist_level)
                    print(GREEN + '\nANSWER\n' + answer + RESET_COLOR + '\n')
                    conversation_history += f"Question: {user_question}\nAnswer: {answer}\n"
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break

        else:
            print("Failed to clone the repository.")
