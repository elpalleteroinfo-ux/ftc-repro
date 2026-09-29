#!/usr/bin/env python
"""Post-install smoke test: verify the package and its full dependency
stack (xesmf/esmpy, cfgrib/eccodes, cartopy, rasterio, ...) import cleanly.
Exercises every model subclass's module (each imports base_downloader.py,
which unconditionally imports xesmf) rather than the old monolithic
UnifiedHRRRDownloader class, which no longer exists in this codebase.
"""
import sys
import traceback

try:
    from UnifiedMETDownloader.UnifiedMETDownloader import RunMETDownloader, main
    from UnifiedMETDownloader.config_loader import load_config, validate_config
    from UnifiedMETDownloader.downloader_factory import create_downloader
    from UnifiedMETDownloader.models.hrrr_model import HRRRDownloader
    from UnifiedMETDownloader.models.rrfs_model import RRFSDownloader
   
except Exception:
    traceback.print_exc()
    sys.exit(1)

sys.exit(0)
