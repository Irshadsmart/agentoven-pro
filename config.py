"""
AGENTOVEN CONFIGURATION - MODIFY THIS FILE TO CHANGE AGENTS & RECIPES

This is the MASTER configuration file for all agent and recipe definitions.
Change values here and they'll automatically apply to all scripts.

TO CREATE A NEW AGENT/RECIPE:
  1. Change the values in this file
  2. Run: python register_recipe.py
  3. Run: python run_recipe_workflow.py
"""

# ============================================================================
# AGENT CONFIGURATION
# ============================================================================
AGENT_NAME = "banking-loan-processor-agent"
AGENT_DESCRIPTION = "A friendly assistant that helps with various tasks"
AGENT_MODEL_PROVIDER = "gemini"
AGENT_MODEL_NAME = "gemini-2.5-flash"
AGENT_SYSTEM_PROMPT = """You are a helpful and professional assistant. Always be clear,
concise, and provide well-structured responses. When processing requests, analyze
thoroughly and provide thoughtful outputs."""
AGENT_ENVIRONMENT = "Prod"

# ============================================================================
# RECIPE CONFIGURATION
# ============================================================================
RECIPE_NAME = "greet-agent-5step-approval-workflow"
RECIPE_FOLDER = "greet-agent-5step-approval-workflow"  # Folder name matching recipe
RECIPE_VERSION = "v1.0.0"
RECIPE_DESCRIPTION = """End-to-end home loan approval workflow.
Process: Application intake → Document verification & credit analysis → Credit appraisal draft →
Credit Manager approval gate → Sanction/decline letter generation.
Demonstrates human-in-the-loop decision making for ₹45L home loan with 20-year tenure."""
RECIPE_AUTHOR = "AgentOven Team"
RECIPE_ENVIRONMENT = "Prod"
RECIPE_TAGS = ["human-gate", "approval", "workflow", "multi-step"]

# ============================================================================
# STEP DEFINITIONS - The 5 Steps in Your Recipe
# ============================================================================
# Change these as needed. Each step will appear in DishShelf in order.

# STEP 1: Application Intake
STEP_1_ID = "collect-input"
STEP_1_TYPE = "agent"
STEP_1_TITLE = "Application Intake & Registration"
STEP_1_DESCRIPTION = "Registers the loan application and extracts key details: applicant, product, amount, tenure, branch."
STEP_1_AGENT = AGENT_NAME
STEP_1_PROMPT = "You are a banking loan processor. The applicant has submitted a home loan application: {{input.user_text}}. Extract and document: 1) Application ID, 2) Applicant name, 3) Loan product, 4) Loan amount (₹), 5) Tenure (years), 6) Branch. Structure your response clearly with all details organized."

# STEP 2: Document Verification & Credit Analysis
STEP_2_ID = "analyze"
STEP_2_TYPE = "agent"
STEP_2_TITLE = "Document Verification & Credit Analysis"
STEP_2_DESCRIPTION = "Verifies all required documents (PAN, Aadhaar, salary slips, bank statements) and performs credit analysis (FOIR, risk assessment)."
STEP_2_AGENT = AGENT_NAME
STEP_2_PROMPT = "You are a credit analyst. Based on this application: {{steps.collect-input.output}}, perform a credit analysis: 1) Check if all documents are present and valid, 2) Verify applicant details across documents, 3) Analyze income stability, 4) Calculate FOIR (fixed obligation to income ratio), 5) Identify any risk flags or inconsistencies. Provide a structured analysis with findings."

# STEP 3: Credit Appraisal Draft
STEP_3_ID = "generate-draft"
STEP_3_TYPE = "agent"
STEP_3_TITLE = "Generate Credit Appraisal Note"
STEP_3_DESCRIPTION = "Drafts the credit appraisal note with recommendation (Approve with/without conditions or Decline)."
STEP_3_AGENT = AGENT_NAME
STEP_3_PROMPT = "Based on this analysis: {{steps.analyze.output}}, generate a professional credit appraisal note with: 1) Loan summary, 2) Applicant profile & income analysis, 3) Risk assessment & findings, 4) FOIR & repayment capacity, 5) Final recommendation (Approve/Approve with conditions/Decline), 6) Conditions if any, 7) Comments for Credit Manager. Format as a formal appraisal note."

# STEP 4: Finalization (Post-Approval)
STEP_4_ID = "finalize"
STEP_4_TYPE = "agent"
STEP_4_TITLE = "Generate Sanction/Decline Letter"
STEP_4_DESCRIPTION = "Records the Credit Manager's decision and generates formal sanction or decline letter."
STEP_4_AGENT = AGENT_NAME
STEP_4_PROMPT = "The Credit Manager has reviewed the appraisal: {{steps.generate-draft.output}}. Generate a formal sanction/decline letter: 1) Loan reference & applicant, 2) Approved/declined amount and terms, 3) Conditions or reasons for decline, 4) Next steps, 5) Contact details. Format as an official bank letter."

# STEP 5: Credit Manager Approval Gate - HUMAN DECISION
STEP_5_ID = "human-approval"
STEP_5_TYPE = "human_gate"
STEP_5_TITLE = "Credit Manager Final Approval"
STEP_5_DESCRIPTION = "Credit Manager reviews the appraisal and decides: Approve or Decline. No loan is sanctioned without this human decision."
STEP_5_MESSAGE = "CREDIT MANAGER - Please review the loan application and appraisal below:\n\n{{steps.generate-draft.output}}\n\nDecision required: Approve (Sanction the loan) or Reject (Decline the application)"
STEP_5_TIMEOUT = 3600  # seconds (1 hour for decision)

# ============================================================================
# TEST CONFIGURATION
# ============================================================================
TEST_SAMPLE_INPUT = "What is the capital of France?"
TEST_DECISION = ""  # Leave empty for manual approval in UI

# ============================================================================
# EXAMPLES FOR FUTURE USE
# ============================================================================
"""
To create a new recipe tomorrow, simply change the values above:

EXAMPLE 1: Document Review Recipe
  RECIPE_NAME = "document-review-pipeline"
  RECIPE_DESCRIPTION = "Comprehensive document review workflow..."
  STEP_3_TITLE = "Generate Review Report"

EXAMPLE 2: Customer Support Recipe
  AGENT_NAME = "customer-support-agent"
  RECIPE_NAME = "customer-support-workflow"
  STEP_1_TITLE = "Classify Support Request"
  STEP_3_TITLE = "Generate Solution"

EXAMPLE 3: Content Moderation Recipe
  RECIPE_NAME = "content-moderation-pipeline"
  STEP_2_TITLE = "Analyze Content Safety"
  STEP_4_TITLE = "Moderator Review"

Just update the config.py and all scripts will use the new values!
"""
