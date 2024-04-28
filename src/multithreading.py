# Import the concurrent.futures module to handle a pool of threads for parallel execution
import concurrent.futures

# Define a class to encapsulate multithreading functions
class MultithreadClass:
    # Method to simulate a task, e.g., making a prediction or processing
    def pred(self, i):
        # Returns a dictionary representing a simulated process with a name and time cost
        return {"process_name": f"Process_{i}", "process_time": i}

    # Method to handle multithreading
    def do_multithreading(self, hit):
        # Use ThreadPoolExecutor to manage a pool of threads; max_workers defines the maximum number of threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            # Create a dictionary of future objects to keep track of the tasks; each task runs 'pred' method
            future_to_i = {executor.submit(self.pred, i): i for i in hit}

        # Initialize a dictionary to store the time taken by each process
        time_dict = {}
        # List to collect responses from each task
        responses = []

        # Process completed tasks as they finish
        for future in concurrent.futures.as_completed(future_to_i):
            try:
                # Get the result of the future object which is the response from 'pred' method
                response = future.result()
                if response:
                    # Append the response dictionary to the responses list
                    responses.append(response)
                    # Map process name to process time in time_dict
                    time_dict[response.get("process_name")] = response.get("process_time")
            except Exception as e:
                # Handle exceptions that might have occurred in tasks
                print(f"Task raised an exception: {e}")
        # Return the list of responses
        return responses

# Check if the script is run as the main program
if __name__ == "__main__":
    # Create an instance of MultithreadClass
    my_class = MultithreadClass()
    # List of inputs to be processed by threads
    hit = [1, 2, 3, 4]
    # Execute the multithreading method and print the responses
    responses = my_class.do_multithreading(hit)
    print(responses)
