from agent import Agent

repo_url = input("GitHub repo URL: ")
question = input("Question: ")

agent = Agent()

response = agent.run(f"{question}\n\nRepo: {repo_url}")

print(response)