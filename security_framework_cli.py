#!/usr/bin/env python3

import os
import sys
import yaml
import argparse
from typing import Dict, Optional
import questionary
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
import asyncio
from security_ai_agent import SecurityAIAgent

class SecurityFrameworkCLI:
    def __init__(self):
        self.config = {}
        self.console = Console()
        self.ai_agent = SecurityAIAgent()
        self._load_config()

    # Rest of the SecurityFrameworkCLI class code...