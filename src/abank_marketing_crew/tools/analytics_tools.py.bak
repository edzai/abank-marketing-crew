"""Analytics Tools"""

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json


class MetricsInput(BaseModel):
    campaign_id: str = Field(..., description="Campaign ID")


class CampaignMetricsTracker(BaseTool):
    name: str = "Campaign Metrics Tracker"
    description: str = "Track campaign performance"
    args_schema: Type[BaseModel] = MetricsInput
    
    def _run(self, campaign_id: str) -> str:
        return json.dumps({"ctr": 3.5, "conversion_rate": 2.1, "roi": 245}, indent=2)


class AttributionInput(BaseModel):
    journey_data: str = Field(..., description="Customer journey data")


class AttributionModeler(BaseTool):
    name: str = "Attribution Modeler"
    description: str = "Model attribution"
    args_schema: Type[BaseModel] = AttributionInput
    
    def _run(self, journey_data: str) -> str:
        return json.dumps({"model": "data-driven", "accuracy": 0.87}, indent=2)


class ROIInput(BaseModel):
    spend: float = Field(..., description="Campaign spend")
    revenue: float = Field(..., description="Revenue generated")


class ROICalculator(BaseTool):
    name: str = "ROI Calculator"
    description: str = "Calculate ROI"
    args_schema: Type[BaseModel] = ROIInput
    
    def _run(self, spend: float, revenue: float) -> str:
        roi = ((revenue - spend) / spend) * 100
        return json.dumps({"roi_percent": round(roi, 2), "profit": revenue - spend}, indent=2)
