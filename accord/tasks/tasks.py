"""General task module."""

"""Tasks"""
from deode.logs import logger
from deode.tasks.base import Task

from accord.data_assimilation import get_odb

class TestJob(Task):
    """Test task class for ACCORD."""

    def __init__(self, config):
        """Construct test class.

        Args:
        ----
            config (ParsedConfig): Configuration.
            name (str): Task name.

        """
        Task.__init__(self, config, "TestJob")
        logger.info("Running {}", self.name)
        logger.info("ODB: {}", get_odb())

