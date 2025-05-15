import logging
from .config import Config

# 로깅 설정
logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)

try:
    assert hasattr(Config, 'SQLALCHEMY_DATABASE_URI'), "Config 클래스가 잘못 정의되었습니다."
    logger.info("Config 모듈이 올바르게 로드되었습니다.")
except AssertionError as e:
    logger.error(f"Config 로드 실패: {e}")
except Exception as e:
    logger.error(f"예상치 못한 오류: {e}")