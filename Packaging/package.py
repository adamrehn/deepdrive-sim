#!/usr/bin/env python3
from ue4helpers import FilesystemUtils, ProjectPackager, UnrealUtils
from os.path import abspath, dirname, join

# Compute the absolute path to the root of the repository
root = dirname(dirname(abspath(__file__)))

# TODO: download our plugin zip files from AWS if the local versions don't exist

# Download and extract the prebuilt binaries for the Substance plugin
print('Downloading and extracting the prebuilt Substance plugin...')
UnrealUtils.install_plugin(join(root, 'Packaging', 'Substance-4.21.0.31-Desktop.zip'), 'Substance', prefix='Marketplace')

# Download and extract the prebuilt binaries for the UnrealEnginePython plugin
print('Downloading and extracting the prebuilt UnrealEnginePython plugin...')
UnrealUtils.install_plugin(join(root, 'Packaging', 'UnrealEnginePython-20181229-Linux.zip'), 'UnrealEnginePython')

# Create our project packager
packager = ProjectPackager(
	root = root,
	version = FilesystemUtils.read(join(root, 'Content', 'Data', 'VERSION')),
	archive = '{name}-{version}-{platform}'
)

# Clean any previous build artifacts
packager.clean()

# Package the project
packager.package()

# Compress the packaged distribution
archive = packager.archive()

# TODO: upload the archive to Amazon S3
print('Created compressed archive "{}".'.format(archive))
