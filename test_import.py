import sys
print("Python path:", sys.path)

try:
    import six
    print("Successfully imported six")
except ImportError as e:
    print("Error importing six:", e)

try:
    from nixtla import NixtlaClient
    print("Successfully imported NixtlaClient from nixtla")
except ImportError as e:
    print("Error importing NixtlaClient from nixtla:", e)
