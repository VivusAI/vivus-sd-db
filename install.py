import launch

if not launch.is_installed("pymongo"):
    launch.run_pip("install pymongo", "requirements for vivus-sd-db")

if not launch.is_installed("tssplit"):
    launch.run_pip("install tssplit", "requirements for vivus-sd-db")