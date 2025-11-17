#!/usr/bin/env python
"""
Quick Start Example - ABank Marketing Crew

This script demonstrates how to run a simple product launch workflow.
"""

import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set a dummy API key for demonstration (replace with real key)
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "sk-demo-key-replace-with-real-key"

from abank_marketing_crew.crew import create_crew

def main():
    """Run a quick product launch example"""
    
    print("\n" + "="*60)
    print(" ABank Marketing Crew - Quick Start Example")
    print("="*60 + "\n")
    
    # Define workflow inputs
    inputs = {
        "product_name": "Youth Digital Savings Account",
        "launch_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
        "target_regions": "Gauteng, Western Cape, KwaZulu-Natal",
        "campaign_budget": "R500,000",
        "product_features": "Zero monthly fees, 5% interest, mobile-first, instant account opening",
        "pricing_strategy": "Competitive positioning against FNB Easy and Capitec Global One",
        "campaign_duration": "3 months",
        "success_criteria": "50,000 new accounts, R250M in deposits, NPS >70"
    }
    
    print("Workflow: Product Launch Campaign")
    print(f"Product: {inputs['product_name']}")
    print(f"Launch Date: {inputs['launch_date']}")
    print(f"Budget: {inputs['campaign_budget']}\n")
    
    print("Creating marketing crew...")
    
    try:
        # Create the crew
        crew = create_crew(workflow="product_launch", verbose=True)
        
        print("\nExecuting workflow...\n")
        print("-" * 60)
        
        # Execute the workflow
        result = crew.kickoff(inputs=inputs)
        
        print("\n" + "="*60)
        print(" Workflow Completed Successfully!")
        print("="*60 + "\n")
        
        print("Result Summary:")
        print("-" * 60)
        print(str(result)[:500] + "..." if len(str(result)) > 500 else str(result))
        print("-" * 60)
        
        # Save result
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"product_launch_result_{timestamp}.txt"
        
        with open(output_file, 'w') as f:
            f.write("ABank Marketing Crew - Product Launch Result\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write(f"Product: {inputs['product_name']}\n\n")
            f.write("Full Result:\n")
            f.write("-" * 60 + "\n")
            f.write(str(result))
        
        print(f"\nFull result saved to: {output_file}\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")
        print("Make sure you have set up your .env file with valid API keys.")
        print("See .env.example for required configuration.\n")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
