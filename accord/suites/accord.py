"""Offline suite."""
from pathlib import Path

from deode import GeneralConstants
from deode.datetime_utils import as_datetime, as_timedelta, get_decadal_list, get_decade
from deode.logs import logger
from deode.suites.base import (
    EcflowSuiteFamily,
    EcflowSuiteTask,
    EcflowSuiteTrigger,
    EcflowSuiteTriggers,
    SuiteDefinition,
)

class AccordSuiteDefinition(SuiteDefinition):
    """Surfex suite."""

    def __init__(
        self,
        config,
        dry_run=False,
    ):
        """Initialize a SurfexSuite object.

        Args:
        ----
            suite_name (str): Name of the suite
            config (ParsedConfig): Parsed configuration
            dry_run (str, optional): Dry run. Defaults to False

        Raises:
        ------
            NotImplementedError: Not implmented

        """
        SuiteDefinition.__init__(self, config, dry_run=dry_run)

        realization = None
        deode_dir = GeneralConstants.PACKAGE_DIRECTORY
        template = deode_dir.resolve() / "templates/ecflow/default.py"
        template = template.as_posix()

        basetime = as_datetime(config["general.times.basetime"])
        starttime = as_datetime(config["general.times.start"])
        endtime = as_datetime(config["general.times.end"])
        cycle_length = as_timedelta(config["general.times.cycle_length"])
        logger.debug("DTGSTART: {} DTGBEG: {} DTGEND: {}", basetime, starttime, endtime)

        test_fam = EcflowSuiteFamily("TestFam", self.suite, self.ecf_files)
        EcflowSuiteTask(
                    "TestJob",
                    test_fam,
                    config,
                    self.task_settings,
                    self.ecf_files,
                    input_template=template,
        )

