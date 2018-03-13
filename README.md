# httpResponder
This is a tool that sets up 3 HTTP endpoints. The hostname/IP and the port number is configurable.
The tool accepts POST messages on each endpoints (and saves them on the hard drive) and sends back a response (which is configurable).

I created this little tool to test an application where the software posted messages and expected a response in exchange (and used that response further down the line..).
Using this tool I was able to stress the message flow back and forth while checking the incoming requests and sending back responses with different structure and values to ensure every scenario works as designed.
