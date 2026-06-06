
import SwiftUI

struct ContentView: View {
    @State private var apiEndpoint = ""
    @State private var jsonMessage = ""
    @State private var responseMessage = ""


    var body: some View {
        VStack {
            TextField("API Endpoint", text: $apiEndpoint)
                .padding()
            TextField("JSON Message", text: $jsonMessage)
                .padding()
            Button("Send POST Request") {
                // Action to perform POST request
                guard let jsonData = jsonMessage.data(using: .utf8) else { return }

                    NetworkManager.shared.postRequest(endpoint: apiEndpoint, jsonData: jsonData) { result in
                        switch result {
                        case .success(let response):
                            print("Response: \(response)")
                        case .failure(let error):
                            print("Error: \(error.localizedDescription)")
                        }
                    }
                
            }
            .padding()
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
