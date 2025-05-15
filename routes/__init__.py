# Import all blueprint modules
from .upload import upload_bp
from .summarize import summarize_bp
from .edit import edit_bp
from .status import status_bp
from .dashboard import dashboard_bp

# Export all blueprints
__all__ = [
    'upload_bp',
    'summarize_bp',
    'edit_bp',
    'status_bp',
    'dashboard_bp'
]