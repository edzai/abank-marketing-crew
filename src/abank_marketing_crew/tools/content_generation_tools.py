"""
Content Generation Tools for Content Strategy Agent
"""

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json


class ContentGeneratorInput(BaseModel):
    content_type: str = Field(..., description="Type: email, sms, social, blog, ad_copy")
    brief: str = Field(..., description="Creative brief")
    tone: str = Field(default="professional", description="Tone")


class ContentGenerator(BaseTool):
    name: str = "Content Generator"
    description: str = "Generate marketing content"
    args_schema: Type[BaseModel] = ContentGeneratorInput
    
    def _run(self, content_type: str, brief: str, tone: str = "professional") -> str:
        return json.dumps({"content_type": content_type, "generated": f"{tone} content for {brief}"}, indent=2)


class BrandGuidelinesInput(BaseModel):
    content: str = Field(..., description="Content to check")


class BrandGuidelinesChecker(BaseTool):
    name: str = "Brand Guidelines Checker"
    description: str = "Check content against brand guidelines"
    args_schema: Type[BaseModel] = BrandGuidelinesInput
    
    def _run(self, content: str) -> str:
        return json.dumps({"compliance_score": 0.95, "status": "approved"}, indent=2)


class MultilingualInput(BaseModel):
    text: str = Field(..., description="Text to translate")
    target_languages: str = Field(..., description="Language codes")


class MultilingualTranslator(BaseTool):
    name: str = "Multilingual Translator"
    description: str = "Translate to SA languages"
    args_schema: Type[BaseModel] = MultilingualInput
    
    def _run(self, text: str, target_languages: str) -> str:
        return json.dumps({lang.strip(): f"[{lang} translation]" for lang in target_languages.split(",")}, indent=2)
