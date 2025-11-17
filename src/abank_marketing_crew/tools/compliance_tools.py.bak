"""Compliance Tools"""

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json


class RegulatoryDBInput(BaseModel):
    query: str = Field(..., description="Regulation query")


class RegulatoryDatabase(BaseTool):
    name: str = "Regulatory Database"
    description: str = "Query banking regulations"
    args_schema: Type[BaseModel] = RegulatoryDBInput
    
    def _run(self, query: str) -> str:
        return json.dumps({"regulations": ["TCF", "POPIA", "FAIS"], "status": "current"}, indent=2)


class ComplianceScanInput(BaseModel):
    content: str = Field(..., description="Content to scan")


class ComplianceScanner(BaseTool):
    name: str = "Compliance Scanner"
    description: str = "Scan for compliance issues"
    args_schema: Type[BaseModel] = ComplianceScanInput
    
    def _run(self, content: str) -> str:
        return json.dumps({"compliance_score": 0.98, "issues": [], "approved": True}, indent=2)


class RiskScoringInput(BaseModel):
    campaign_details: str = Field(..., description="Campaign details")


class RiskScoringTool(BaseTool):
    name: str = "Risk Scoring Tool"
    description: str = "Score campaign risk"
    args_schema: Type[BaseModel] = RiskScoringInput
    
    def _run(self, campaign_details: str) -> str:
        return json.dumps({"risk_score": 15, "risk_level": "low", "proceed": True}, indent=2)
