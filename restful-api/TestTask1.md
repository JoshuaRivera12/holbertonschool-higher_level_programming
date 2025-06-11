✅ Step 1: Install curl (if not already installed)
Use this command in your terminal:

bash
Copy
Edit
sudo apt update
sudo apt install curl
If you're on macOS, use:

bash
Copy
Edit
brew install curl
You can confirm it's installed by checking the version:

bash
Copy
Edit
curl --version


✅ Step 2: Make a Basic API Request
Try a simple GET request to a public API:

bash
Copy
Edit
curl https://api.github.com
✅ Step 3: Add Headers (e.g., User-Agent)
Some APIs (like GitHub's) require a User-Agent:

bash
Copy
Edit
curl -H "User-Agent: MySchoolProject" https://api.github.com


✅ Step 4: Make a POST Request with Data
Example: Post JSON to a fake API:

bash
Copy
Edit
curl -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title":"hello","body":"world","userId":1}'


✅ Step 5: View HTTP Headers in the Response
Use -i or -v:

bash
Copy
Edit
curl -i https://api.github.com


✅ Summary of Important Options
Option	Purpose
-X	Specify HTTP method (GET, POST, etc.)
-H	Add a custom HTTP header
-d	Send data (usually with POST or PUT)
-i	Include response headers in the output
-v	Verbose mode (more detail about the request)
