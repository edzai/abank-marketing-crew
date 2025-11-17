"""
Validators for workflow inputs and data
"""

from typing import Dict, Any, List
from datetime import datetime


def validate_workflow_inputs(workflow: str, inputs: Dict[str, Any]) -> tuple[bool, List[str]]:
    """
    Validate workflow input parameters.
    
    Args:
        workflow: Workflow type
        inputs: Input parameters dictionary
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    if workflow == "product_launch":
        required_fields = ["product_name", "launch_date"]
        for field in required_fields:
            if field not in inputs or not inputs[field]:
                errors.append(f"Missing required field: {field}")
        
        # Validate date format
        if "launch_date" in inputs:
            try:
                datetime.strptime(inputs["launch_date"], "%Y-%m-%d")
            except ValueError:
                errors.append("Invalid launch_date format. Use YYYY-MM-DD")
    
    elif workflow == "real_time_response":
        if "monitoring_priorities" not in inputs:
            errors.append("Missing monitoring_priorities")
    
    elif workflow == "personalized_journey":
        if "analysis_date" not in inputs:
            errors.append("Missing analysis_date")
    
    return (len(errors) == 0, errors)


def validate_budget(amount: float, max_budget: float = 1000000.0) -> bool:
    """Validate budget amount"""
    return 0 < amount <= max_budget


def validate_phone_number(number: str) -> bool:
    """Validate South African phone number format"""
    import re
    pattern = r'^\+27\d{9}$|^0\d{9}$'
    return bool(re.match(pattern, number))
