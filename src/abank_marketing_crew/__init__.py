"""
ABank Marketing Crew - Autonomous Multi-Agent Marketing System

A CrewAI-based system for orchestrating marketing operations
at ABank using specialized AI agents.
"""

__version__ = "1.0.0"
__author__ = "ABank AI Team"

from abank_marketing_crew.crew import create_crew, MarketingCrew

__all__ = ["create_crew", "MarketingCrew"]
