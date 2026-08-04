

import Foundation

class NetworkManager {
    static let shared = NetworkManager()

    func postRequest(endpoint: String, jsonData: Data, completion: @escaping (Result<String, Error>) -> Void) {
        guard let url = URL(string: endpoint) else {
            completion(.failure(NSError(domain: "", code: -1, userInfo: [NSLocalizedDescriptionKey: "Invalid URL"])))
            return
        }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.httpBody = jsonData
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")

        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                completion(.failure(error))
                return
            }
            if let data = data, let responseString = String(data: data, encoding: .utf8) {
                completion(.success(responseString))
            }
        }.resume()
    }
}

