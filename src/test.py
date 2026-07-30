from agent import Agent

agent = Agent()

response = agent.run(
    "Read README.md and explain this project."
)

print(response)