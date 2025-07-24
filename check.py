import os
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dataclasses import dataclass
from agents import Agent, RunContextWrapper, Runner, function_tool

# 1. Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# 2. Set up Gemini-compatible OpenAI client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 3. Define the model to use
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # adjust if needed
    openai_client=external_client
)

# 4. Runner configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


# 3. Define Context
@dataclass
class user_data:
    name: str
    age: int

# 4. Define Tool Output
class UserOutput(BaseModel):
    name: str
    age: int

# 5. Tool Function
@function_tool
async def get_user_data(wrapper: RunContextWrapper[user_data]) -> UserOutput:
    return UserOutput(
        name=wrapper.context.name,
        age=wrapper.context.age
    )

# 6. Main Execution
async def main():
    context_data = user_data(name="taha", age=20)

    agent = Agent[user_data](
        name="assistant",
        tools=[get_user_data],
        model=model,
        instructions="Use the `get_user_data` tool to fetch name and age."
    )

    result = await Runner.run(
        starting_agent=agent,
        input="What is the user's name and age?",
        context=context_data,
        run_config=config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())





