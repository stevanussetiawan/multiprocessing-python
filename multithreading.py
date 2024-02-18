import concurrent.futures

class MultithreadClass:
    def pred(self, i):
        return {"process_name": f"Process_{i}", "process_time": i}

    def do_multithreading(self, hit):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_to_i = {executor.submit(self.pred, i): i for i in hit}

        time_dict = {}
        responses = []

        for future in concurrent.futures.as_completed(future_to_i):
            try:
                response = future.result()
                if response:
                    responses.append(response)
                    time_dict[response.get("process_name")] = response.get("process_time")
            except Exception as e:
                print(f"Task raised an exception: {e}")
        return responses

if __name__ == "__main__":
    my_class = MultithreadClass()
    hit = [1, 2, 3, 4]
    responses = my_class.do_multithreading(hit)
    print(responses)