which python3
if [[ $? -ne 0 ]]; then echo "Cannot find python3" && exit 255; fi

# version=$(python3 --version | awk '{ print $2 }')
# if [[ $? -ne 0 ]]; then echo "Failed to identify version" && exit 255; fi

#major_version=$(echo -n "${version}" | awk -F "." '{ print $1 }')
#if [[ $? -ne 0 ]]; then echo "Failed to identify major version" && exit 255; fi
#
#minor_version=$(echo -n "${version}" | awk -F "." '{ print $2 }')
#if [[ $? -ne 0 ]]; then echo "Failed to identify minor version" && exit 255; fi
#
#poetry_executable="${HOME}/Library/Python/${major_version}.${minor_version}/bin/poetry"
#if [[ -f "${poetry_executable}" ]]; then
#  echo "Poetry already installed" && exit 0
#else
# Needed to execute /Applications/Python\ 3.9/Install\ Certificates.command
# Without execution, was getting an SSLError
curl -sSL https://install.python-poetry.org | python3 - --version 1.1.12
if [[ $? -ne 0 ]]; then echo "Failed to install Poetry" && exit 255; fi
#fi
