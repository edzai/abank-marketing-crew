#!/usr/bin/env python
"""
ABank Marketing Crew - Main Entry Point

This module provides the CLI interface for running different marketing workflows
and managing the autonomous multi-agent marketing system.
"""

import sys
import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import logging
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from abank_marketing_crew.crew import create_crew, MarketingCrew
from abank_marketing_crew.utils.logging_config import setup_logging
from abank_marketing_crew.utils.validators import validate_workflow_inputs

# Setup logging
logger = setup_logging()
console = Console()


def display_banner():
    """Display welcome banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║          ABank Marketing Crew v1.0.0                      ║
    ║     Autonomous Multi-Agent Marketing System               ║
    ║                                                           ║
    ║     Powered by CrewAI | Built for Innovation             ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    console.print(banner, style="bold cyan")


def run_product_launch_workflow(inputs: Dict[str, Any], verbose: bool = True) -> Dict[str, Any]:
    """
    Execute product launch campaign workflow.
    
    Args:
        inputs: Workflow input parameters including product details
        verbose: Enable verbose logging
        
    Returns:
        Workflow execution results
    """
    console.print("\n[bold green]🚀 Initiating Product Launch Workflow[/bold green]\n")
    
    # Display workflow parameters
    params_table = Table(title="Workflow Parameters")
    params_table.add_column("Parameter", style="cyan")
    params_table.add_column("Value", style="yellow")
    
    for key, value in inputs.items():
        params_table.add_row(key, str(value))
    
    console.print(params_table)
    console.print()
    
    try:
        # Create and run crew
        crew = create_crew(workflow="product_launch", verbose=verbose)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Executing workflow...", total=None)
            
            result = crew.kickoff(inputs=inputs)
            
            progress.update(task, completed=True)
        
        console.print("\n[bold green]✓ Product Launch Workflow Completed Successfully![/bold green]\n")
        
        return {
            "status": "success",
            "workflow": "product_launch",
            "timestamp": datetime.now().isoformat(),
            "result": result
        }
        
    except Exception as e:
        logger.error(f"Product launch workflow failed: {str(e)}", exc_info=True)
        console.print(f"\n[bold red]✗ Workflow Failed: {str(e)}[/bold red]\n")
        return {
            "status": "failed",
            "workflow": "product_launch",
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }


def run_real_time_response_workflow(inputs: Dict[str, Any], verbose: bool = True) -> Dict[str, Any]:
    """
    Execute real-time market response workflow.
    
    Args:
        inputs: Workflow input parameters
        verbose: Enable verbose logging
        
    Returns:
        Workflow execution results
    """
    console.print("\n[bold yellow]⚡ Initiating Real-Time Response Workflow[/bold yellow]\n")
    
    try:
        crew = create_crew(workflow="real_time_response", verbose=verbose)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Monitoring and responding...", total=None)
            
            result = crew.kickoff(inputs=inputs)
            
            progress.update(task, completed=True)
        
        console.print("\n[bold green]✓ Real-Time Response Completed![/bold green]\n")
        
        return {
            "status": "success",
            "workflow": "real_time_response",
            "timestamp": datetime.now().isoformat(),
            "result": result
        }
        
    except Exception as e:
        logger.error(f"Real-time response workflow failed: {str(e)}", exc_info=True)
        console.print(f"\n[bold red]✗ Workflow Failed: {str(e)}[/bold red]\n")
        return {
            "status": "failed",
            "workflow": "real_time_response",
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }


def run_personalized_journey_workflow(inputs: Dict[str, Any], verbose: bool = True) -> Dict[str, Any]:
    """
    Execute personalized customer journey workflow.
    
    Args:
        inputs: Workflow input parameters
        verbose: Enable verbose logging
        
    Returns:
        Workflow execution results
    """
    console.print("\n[bold magenta]👤 Initiating Personalized Journey Workflow[/bold magenta]\n")
    
    try:
        crew = create_crew(workflow="personalized_journey", verbose=verbose)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Personalizing customer journeys...", total=None)
            
            result = crew.kickoff(inputs=inputs)
            
            progress.update(task, completed=True)
        
        console.print("\n[bold green]✓ Personalized Journey Workflow Completed![/bold green]\n")
        
        return {
            "status": "success",
            "workflow": "personalized_journey",
            "timestamp": datetime.now().isoformat(),
            "result": result
        }
        
    except Exception as e:
        logger.error(f"Personalized journey workflow failed: {str(e)}", exc_info=True)
        console.print(f"\n[bold red]✗ Workflow Failed: {str(e)}[/bold red]\n")
        return {
            "status": "failed",
            "workflow": "personalized_journey",
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }


def run_interactive_mode():
    """Run crew in interactive mode with CLI prompts"""
    console.print("\n[bold cyan]🤖 Interactive Mode[/bold cyan]\n")
    
    # Select workflow
    console.print("Available Workflows:")
    console.print("  1. Product Launch Campaign")
    console.print("  2. Real-Time Market Response")
    console.print("  3. Personalized Customer Journey")
    console.print("  4. Exit\n")
    
    choice = console.input("[bold]Select workflow (1-4): [/bold]")
    
    if choice == "1":
        product_name = console.input("[bold]Product Name: [/bold]")
        launch_date = console.input("[bold]Launch Date (YYYY-MM-DD): [/bold]")
        target_regions = console.input("[bold]Target Regions (comma-separated): [/bold]")
        budget = console.input("[bold]Campaign Budget (ZAR): [/bold]")
        
        inputs = {
            "product_name": product_name,
            "launch_date": launch_date,
            "target_regions": target_regions.split(","),
            "campaign_budget": f"R{budget}",
            "product_features": "To be analyzed",
            "pricing_strategy": "To be determined"
        }
        
        run_product_launch_workflow(inputs)
        
    elif choice == "2":
        monitoring_focus = console.input("[bold]Monitoring Focus: [/bold]")
        alert_threshold = console.input("[bold]Alert Threshold (low/medium/high): [/bold]")
        
        inputs = {
            "monitoring_priorities": monitoring_focus,
            "alert_criteria": alert_threshold
        }
        
        run_real_time_response_workflow(inputs)
        
    elif choice == "3":
        analysis_date = datetime.now().strftime("%Y-%m-%d")
        focus_areas = console.input("[bold]Focus Segments: [/bold]")
        
        inputs = {
            "analysis_date": analysis_date,
            "focus_segments": focus_areas,
            "personalization_depth": "individual"
        }
        
        run_personalized_journey_workflow(inputs)
        
    elif choice == "4":
        console.print("\n[bold]Goodbye! 👋[/bold]\n")
        sys.exit(0)
    else:
        console.print("\n[bold red]Invalid choice. Please try again.[/bold red]\n")


def save_results(results: Dict[str, Any], output_dir: str = "outputs"):
    """
    Save workflow results to file.
    
    Args:
        results: Workflow execution results
        output_dir: Directory to save results
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    workflow = results.get("workflow", "unknown")
    filename = f"{workflow}_{timestamp}.json"
    
    filepath = output_path / filename
    
    with open(filepath, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    console.print(f"\n[bold green]Results saved to: {filepath}[/bold green]\n")


def main():
    """Main entry point for CLI"""
    parser = argparse.ArgumentParser(
        description="ABank Marketing Crew - Autonomous Multi-Agent Marketing System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run product launch workflow
  python main.py --workflow product_launch --product "Youth Savings Account"
  
  # Run in monitoring mode
  python main.py --mode monitor
  
  # Interactive mode
  python main.py --interactive
  
  # Generate campaign report
  python main.py --report --campaign-id 12345
        """
    )
    
    parser.add_argument(
        '--workflow',
        choices=['product_launch', 'real_time_response', 'personalized_journey'],
        help='Workflow type to execute'
    )
    
    parser.add_argument(
        '--product',
        help='Product name for product launch workflow'
    )
    
    parser.add_argument(
        '--mode',
        choices=['monitor', 'batch', 'interactive'],
        default='interactive',
        help='Execution mode'
    )
    
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run in interactive mode with CLI prompts'
    )
    
    parser.add_argument(
        '--report',
        action='store_true',
        help='Generate campaign report'
    )
    
    parser.add_argument(
        '--campaign-id',
        help='Campaign ID for reporting'
    )
    
    parser.add_argument(
        '--config',
        help='Path to custom configuration file'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '--save-results',
        action='store_true',
        default=True,
        help='Save results to file (default: True)'
    )
    
    args = parser.parse_args()
    
    # Display banner
    display_banner()
    
    try:
        # Interactive mode
        if args.interactive or (not args.workflow and not args.report):
            run_interactive_mode()
            return
        
        # Report generation
        if args.report:
            console.print("[bold yellow]Report generation not yet implemented[/bold yellow]")
            return
        
        # Workflow execution
        if args.workflow == 'product_launch':
            if not args.product:
                console.print("[bold red]Error: --product required for product_launch workflow[/bold red]")
                return
            
            inputs = {
                "product_name": args.product,
                "launch_date": (datetime.now()).strftime("%Y-%m-%d"),
                "target_regions": ["Gauteng", "Western Cape", "KZN"],
                "campaign_budget": "R500,000",
                "product_features": "High-interest savings, mobile-first, no fees",
                "pricing_strategy": "Competitive rate positioning"
            }
            
            results = run_product_launch_workflow(inputs, verbose=args.verbose)
            
            if args.save_results:
                save_results(results)
        
        elif args.workflow == 'real_time_response':
            inputs = {
                "monitoring_priorities": "competitor_rates,economic_events,social_trends",
                "alert_criteria": "medium"
            }
            
            results = run_real_time_response_workflow(inputs, verbose=args.verbose)
            
            if args.save_results:
                save_results(results)
        
        elif args.workflow == 'personalized_journey':
            inputs = {
                "analysis_date": datetime.now().strftime("%Y-%m-%d"),
                "focus_segments": "high_value,at_risk,dormant",
                "personalization_depth": "individual"
            }
            
            results = run_personalized_journey_workflow(inputs, verbose=args.verbose)
            
            if args.save_results:
                save_results(results)
    
    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]Workflow interrupted by user[/bold yellow]\n")
        sys.exit(1)
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        console.print(f"\n[bold red]Fatal Error: {str(e)}[/bold red]\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
