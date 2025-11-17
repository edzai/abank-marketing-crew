import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for API key
if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
    print("\n⚠️  No API key found!")
    print("Please add your API key to the .env file:")
    print("  OPENAI_API_KEY=sk-your-key-here")
    print("  OR")
    print("  ANTHROPIC_API_KEY=sk-ant-your-key-here")
    exit(1)

print("\n" + "="*60)
print(" ABank Marketing Crew - Quick Start Example")
print("="*60 + "\n")

from crewai import Agent, Task, Crew, Process

# Create a simple test agent (without custom tools)
market_analyst = Agent(
    role="Market Intelligence Analyst",
    goal="Analyze the South African banking market for new product opportunities",
    backstory="""You are an expert market analyst with 15 years of experience
    in the South African financial services sector. You understand consumer
    behavior, competitive dynamics, and market trends.""",
    verbose=True,
    allow_delegation=False
)

content_strategist = Agent(
    role="Content Marketing Strategist",
    goal="Develop compelling marketing campaigns for banking products",
    backstory="""You are an award-winning marketing strategist with deep
    understanding of South African culture and demographics. You create
    campaigns that resonate with diverse audiences.""",
    verbose=True,
    allow_delegation=False
)

# Create simple tasks
market_analysis_task = Task(
    description="""Analyze the market opportunity for a new Youth Digital
    Savings Account in South Africa. Consider:
    - Target audience (18-25 year olds)
    - Competitive landscape
    - Key features needed
    - Pricing strategy

    Provide a brief market analysis with recommendations.""",
    expected_output="""A market analysis report with:
    - Target audience profile
    - 3-5 competitor products
    - Recommended features
    - Pricing recommendation""",
    agent=market_analyst
)

content_strategy_task = Task(
    description="""Based on the market analysis, develop a content strategy
    for launching the Youth Digital Savings Account. Include:
    - Key messaging themes
    - Channel recommendations
    - Content ideas for social media

    Keep it focused on digital-first approach.""",
    expected_output="""A content strategy document with:
    - 3 key messaging pillars
    - Recommended marketing channels
    - 5 social media post ideas""",
    agent=content_strategist,
    context=[market_analysis_task]
)

# Create and run the crew
print("Workflow: Product Launch Campaign")
print("Product: Youth Digital Savings Account")
print("Budget: R500,000\n")

print("Creating marketing crew...")
print("-" * 60)

crew = Crew(
    agents=[market_analyst, content_strategist],
    tasks=[market_analysis_task, content_strategy_task],
    process=Process.sequential,
    verbose=True
)

print("\nExecuting workflow...\n")
print("=" * 60)

try:
    result = crew.kickoff()

    print("\n" + "="*60)
    print(" Workflow Completed Successfully!")
    print("="*60 + "\n")

    print("Result Summary:")
    print("-" * 60)
    print(str(result))
    print("-" * 60)

    # Save result
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"test_result_{timestamp}.txt"

    with open(output_file, 'w') as f:
        f.write("ABank Marketing Crew - Test Result\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Product: Youth Digital Savings Account\n\n")
        f.write("Result:\n")
        f.write("-" * 60 + "\n")
        f.write(str(result))

    print(f"\n✅ Full result saved to: {output_file}\n")
    print("🎉 Success! The crew is working properly.\n")

except Exception as e:
    print(f"\n❌ Error: {str(e)}\n")
    import traceback
    traceback.print_exc()
    exit(1)
