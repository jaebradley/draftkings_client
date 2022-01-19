which python3
if [[ $? -ne 0 ]]; then echo "Cannot find python3" && exit 255; fi

# Needed to execute /Applications/Python\ 3.9/Install\ Certificates.command
# Without execution, was getting an SSLError
curl -sSL https://install.python-poetry.org | python3 - --version 1.1.12
if [[ $? -ne 0 ]]; then echo "Failed to install poetry" && exit 255; fi