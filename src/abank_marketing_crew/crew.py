"""
ABank Marketing Crew - Main Orchestration Module

This module defines the MarketingCrew class which orchestrates all agents
and workflows for ABank's autonomous marketing operations.
"""

from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from typing import List, Dict, Any, Optional
import yaml
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import custom tools
from abank_marketing_crew.tools.market_research_tools import (
    WebSearchTool,
    SocialSentimentAnalyzer,
    CompetitorMonitor,
    GoogleTrendsTool
)
from abank_marketing_crew.tools.crm_integration_tools import (
    CRMDataConnector,
    CustomerAnalyticsEngine,
    SegmentationAlgorithm
)
from abank_marketing_crew.tools.content_generation_tools import (
    ContentGenerator,
    BrandGuidelinesChecker,
    MultilingualTranslator
)
from abank_marketing_crew.tools.campaign_deployment_tools import (
    EmailMarketingPlatform,
    SMSGateway,
    SocialMediaPublisher
)
from abank_marketing_crew.tools.analytics_tools import (
    CampaignMetricsTracker,
    AttributionModeler,
    ROICalculator
)
from abank_marketing_crew.tools.compliance_tools import (
    RegulatoryDatabase,
    ComplianceScanner,
    RiskScoringTool
)


@CrewBase
class MarketingCrew:
    """
    ABank Marketing Crew - Autonomous Multi-Agent Marketing System
    
    Orchestrates six specialized agents working collaboratively on complex
    marketing workflows including product launches, real-time responses,
    and personalized customer journeys.
    """
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self, verbose: bool = True):
        """
        Initialize the Marketing Crew with configuration.
        
        Args:
            verbose: Enable verbose logging for agent activities
        """
        self.verbose = verbose
        self.load_configs()
        
    def load_configs(self):
        """Load agent and task configurations from YAML files"""
        config_dir = Path(__file__).parent / 'config'
        
        with open(config_dir / 'agents.yaml', 'r') as f:
            self.agents_config_data = yaml.safe_load(f)
            
        with open(config_dir / 'tasks.yaml', 'r') as f:
            self.tasks_config_data = yaml.safe_load(f)
    
    # =========================================================================
    # AGENT DEFINITIONS
    # =========================================================================
    
    @agent
    def market_intelligence_agent(self) -> Agent:
        """
        Market Intelligence Agent
        
        Monitors and analyzes the South African banking market for opportunities,
        threats, and competitive intelligence.
        """
        config = self.agents_config_data['market_intelligence_agent']
        
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', True),
            max_iter=config.get('max_iter', 15),
            max_rpm=config.get('max_rpm', 60),
            inject_date=config.get('inject_date', True),
            date_format=config.get('date_format', '%B %d, %Y'),
            reasoning=config.get('reasoning', True),
            max_reasoning_attempts=config.get('max_reasoning_attempts', 3),
            tools=[
                WebSearchTool(),
                SocialSentimentAnalyzer(),
                CompetitorMonitor(),
                GoogleTrendsTool()
            ]
        )
    
    @agent
    def customer_segmentation_agent(self) -> Agent:
        """
        Customer Segmentation Agent
        
        Analyzes customer data to create dynamic segments and enable
        hyper-personalized marketing strategies.
        """
        config = self.agents_config_data['customer_segmentation_agent']
        
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', False),
            max_iter=config.get('max_iter', 20),
            max_rpm=config.get('max_rpm', 40),
            reasoning=config.get('reasoning', True),
            max_reasoning_attempts=config.get('max_reasoning_attempts', 4),
            tools=[
                CRMDataConnector(),
                CustomerAnalyticsEngine(),
                SegmentationAlgorithm()
            ]
        )
    
    @agent
    def content_strategy_agent(self) -> Agent:
        """
        Content Strategy Agent
        
        Develops compelling, culturally relevant marketing campaigns and
        content strategies for diverse South African audiences.
        """
        config = self.agents_config_data['content_strategy_agent']
        
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', True),
            max_iter=config.get('max_iter', 18),
            max_rpm=config.get('max_rpm', 50),
            multimodal=config.get('multimodal', True),
            reasoning=config.get('reasoning', True),
            max_reasoning_attempts=config.get('max_reasoning_attempts', 3),
            inject_date=config.get('inject_date', True),
            tools=[
                ContentGenerator(),
                BrandGuidelinesChecker(),
                MultilingualTranslator()
            ]
        )
    
    @agent
    def campaign_execution_agent(self) -> Agent:
        """
        Campaign Execution Agent
        
        Executes marketing campaigns across multiple channels with precision
        and manages deployment, testing, and optimization.
        """
        config = self.agents_config_data['campaign_execution_agent']
        
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', False),
            max_iter=config.get('max_iter', 15),
            max_rpm=config.get('max_rpm', 70),
            tools=[
                EmailMarketingPlatform(),
                SMSGateway(),
                SocialMediaPublisher()
            ]
        )
    
    @agent
    def performance_analytics_agent(self) -> Agent:
        """
        Performance Analytics Agent
        
        Monitors campaign performance, generates insights, and recommends
        data-driven optimizations.
        """
        config = self.agents_config_data['performance_analytics_agent']
        
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', True),
            max_iter=config.get('max_iter', 20),
            max_rpm=config.get('max_rpm', 80),
            reasoning=config.get('reasoning', True),
            max_reasoning_attempts=config.get('max_reasoning_attempts', 4),
            inject_date=config.get('inject_date', True),
            tools=[
                CampaignMetricsTracker(),
                AttributionModeler(),
                ROICalculator()
            ]
        )
    
    @agent
    def compliance_risk_agent(self) -> Agent:
        """
        Compliance & Risk Agent
        
        Ensures all marketing activities comply with South African banking
        regulations and protects brand reputation.
        """
        config = self.agents_config_data['compliance_risk_agent']
        
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=config.get('verbose', True),
            allow_delegation=config.get('allow_delegation', False),
            max_iter=config.get('max_iter', 12),
            max_rpm=config.get('max_rpm', 30),
            reasoning=config.get('reasoning', True),
            max_reasoning_attempts=config.get('max_reasoning_attempts', 2),
            tools=[
                RegulatoryDatabase(),
                ComplianceScanner(),
                RiskScoringTool()
            ]
        )
    
    # =========================================================================
    # TASK DEFINITIONS - PRODUCT LAUNCH WORKFLOW
    # =========================================================================
    
    @task
    def product_launch_market_analysis(self) -> Task:
        """Market analysis task for product launch"""
        config = self.tasks_config_data['product_launch_market_analysis']
        
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.market_intelligence_agent()
        )
    
    @task
    def product_launch_segmentation(self) -> Task:
        """Customer segmentation task for product launch"""
        config = self.tasks_config_data['product_launch_segmentation']
        
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.customer_segmentation_agent(),
            context=[self.product_launch_market_analysis()]
        )
    
    @task
    def product_launch_content_strategy(self) -> Task:
        """Content strategy development for product launch"""
        config = self.tasks_config_data['product_launch_content_strategy']
        
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.content_strategy_agent(),
            context=[
                self.product_launch_market_analysis(),
                self.product_launch_segmentation()
            ]
        )
    
    @task
    def product_launch_compliance_review(self) -> Task:
        """Compliance review for product launch campaign"""
        config = self.tasks_config_data['product_launch_compliance_review']
        
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.compliance_risk_agent(),
            context=[self.product_launch_content_strategy()]
        )
    
    @task
    def product_launch_execution_plan(self) -> Task:
        """Execution planning for product launch"""
        config = self.tasks_config_data['product_launch_execution_plan']
        
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.campaign_execution_agent(),
            context=[
                self.product_launch_content_strategy(),
                self.product_launch_compliance_review()
            ]
        )
    
    @task
    def product_launch_performance_monitoring(self) -> Task:
        """Performance monitoring setup for product launch"""
        config = self.tasks_config_data['product_launch_performance_monitoring']
        
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.performance_analytics_agent(),
            context=[self.product_launch_execution_plan()]
        )
    
    # =========================================================================
    # CREW DEFINITIONS
    # =========================================================================
    
    @crew
    def product_launch_crew(self) -> Crew:
        """
        Product Launch Crew
        
        Orchestrates end-to-end product launch campaign from market analysis
        to deployment and monitoring.
        """
        return Crew(
            agents=[
                self.market_intelligence_agent(),
                self.customer_segmentation_agent(),
                self.content_strategy_agent(),
                self.compliance_risk_agent(),
                self.campaign_execution_agent(),
                self.performance_analytics_agent()
            ],
            tasks=[
                self.product_launch_market_analysis(),
                self.product_launch_segmentation(),
                self.product_launch_content_strategy(),
                self.product_launch_compliance_review(),
                self.product_launch_execution_plan(),
                self.product_launch_performance_monitoring()
            ],
            process=Process.sequential,
            verbose=self.verbose,
            memory=True,
            embedder={
                "provider": "openai",
                "config": {
                    "model": "text-embedding-3-small"
                }
            }
        )
    
    @crew
    def real_time_response_crew(self) -> Crew:
        """
        Real-Time Response Crew
        
        Monitors market conditions and executes rapid response campaigns
        to capitalize on opportunities or mitigate threats.
        """
        # Define real-time workflow tasks
        market_monitoring = Task(
            description=self.tasks_config_data['real_time_market_monitoring']['description'],
            expected_output=self.tasks_config_data['real_time_market_monitoring']['expected_output'],
            agent=self.market_intelligence_agent()
        )
        
        response_strategy = Task(
            description=self.tasks_config_data['real_time_response_strategy']['description'],
            expected_output=self.tasks_config_data['real_time_response_strategy']['expected_output'],
            agent=self.content_strategy_agent(),
            context=[market_monitoring]
        )
        
        compliance_check = Task(
            description=self.tasks_config_data['real_time_compliance_check']['description'],
            expected_output=self.tasks_config_data['real_time_compliance_check']['expected_output'],
            agent=self.compliance_risk_agent(),
            context=[response_strategy]
        )
        
        campaign_deployment = Task(
            description=self.tasks_config_data['real_time_campaign_deployment']['description'],
            expected_output=self.tasks_config_data['real_time_campaign_deployment']['expected_output'],
            agent=self.campaign_execution_agent(),
            context=[compliance_check]
        )
        
        impact_measurement = Task(
            description=self.tasks_config_data['real_time_impact_measurement']['description'],
            expected_output=self.tasks_config_data['real_time_impact_measurement']['expected_output'],
            agent=self.performance_analytics_agent(),
            context=[campaign_deployment]
        )
        
        return Crew(
            agents=[
                self.market_intelligence_agent(),
                self.content_strategy_agent(),
                self.compliance_risk_agent(),
                self.campaign_execution_agent(),
                self.performance_analytics_agent()
            ],
            tasks=[
                market_monitoring,
                response_strategy,
                compliance_check,
                campaign_deployment,
                impact_measurement
            ],
            process=Process.sequential,
            verbose=self.verbose,
            memory=True
        )
    
    @crew
    def personalized_journey_crew(self) -> Crew:
        """
        Personalized Journey Crew
        
        Creates and executes individualized customer journeys with
        hyper-personalized content and automated deployment.
        """
        # Define personalization workflow tasks
        micro_segmentation = Task(
            description=self.tasks_config_data['journey_micro_segmentation']['description'],
            expected_output=self.tasks_config_data['journey_micro_segmentation']['expected_output'],
            agent=self.customer_segmentation_agent()
        )
        
        personalized_content = Task(
            description=self.tasks_config_data['journey_personalized_content']['description'],
            expected_output=self.tasks_config_data['journey_personalized_content']['expected_output'],
            agent=self.content_strategy_agent(),
            context=[micro_segmentation]
        )
        
        automated_deployment = Task(
            description=self.tasks_config_data['journey_automated_deployment']['description'],
            expected_output=self.tasks_config_data['journey_automated_deployment']['expected_output'],
            agent=self.campaign_execution_agent(),
            context=[personalized_content]
        )
        
        engagement_analysis = Task(
            description=self.tasks_config_data['journey_engagement_analysis']['description'],
            expected_output=self.tasks_config_data['journey_engagement_analysis']['expected_output'],
            agent=self.performance_analytics_agent(),
            context=[automated_deployment]
        )
        
        return Crew(
            agents=[
                self.customer_segmentation_agent(),
                self.content_strategy_agent(),
                self.campaign_execution_agent(),
                self.performance_analytics_agent()
            ],
            tasks=[
                micro_segmentation,
                personalized_content,
                automated_deployment,
                engagement_analysis
            ],
            process=Process.sequential,
            verbose=self.verbose,
            memory=True
        )


def create_crew(workflow: str = "product_launch", **kwargs) -> Crew:
    """
    Factory function to create specific crew based on workflow type.
    
    Args:
        workflow: Type of workflow ('product_launch', 'real_time_response', 'personalized_journey')
        **kwargs: Additional arguments to pass to the crew
        
    Returns:
        Configured Crew instance
    """
    marketing_crew = MarketingCrew(verbose=kwargs.get('verbose', True))
    
    if workflow == "product_launch":
        return marketing_crew.product_launch_crew()
    elif workflow == "real_time_response":
        return marketing_crew.real_time_response_crew()
    elif workflow == "personalized_journey":
        return marketing_crew.personalized_journey_crew()
    else:
        raise ValueError(f"Unknown workflow type: {workflow}")
