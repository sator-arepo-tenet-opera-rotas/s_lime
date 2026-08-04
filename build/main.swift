import Cocoa

// Model
class Model {
    var inputText: String = ""
    var outputText: String = ""
}

// View
class View: NSView {
    let inputTextField: NSTextField
    let outputTextField: NSTextField
    let button: NSButton
    
    var controller: Controller?
    
    override init(frame frameRect: NSRect) {
        inputTextField = NSTextField()
        outputTextField = NSTextField()
        button = NSButton(title: "Process", target: nil, action: #selector(processButtonClicked))
        
        super.init(frame: frameRect)
        
        inputTextField.frame = NSRect(x: 20, y: 100, width: 200, height: 24)
        outputTextField.frame = NSRect(x: 20, y: 60, width: 200, height: 24)
        button.frame = NSRect(x: 230, y: 100, width: 60, height: 24)
        
        outputTextField.isEditable = false
        
        addSubview(inputTextField)
        addSubview(outputTextField)
        addSubview(button)
    }
    
    required init?(coder decoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    @objc func processButtonClicked() {
        controller?.processInput()
    }
}

// Controller
class Controller {
    let model: Model
    let view: View
    
    init(model: Model, view: View) {
        self.model = model
        self.view = view
        self.view.controller = self
    }
    
    func processInput() {
        model.outputText = model.inputText
        view.outputTextField.stringValue = model.outputText
    }
}

// Application Delegate
class AppDelegate: NSObject, NSApplicationDelegate {
    let window: NSWindow
    let view: View
    let controller: Controller
    
    override init() {
        view = View(frame: NSRect(x: 0, y: 0, width: 300, height: 150))
        let model = Model()
        controller = Controller(model: model, view: view)
        
        window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 300, height: 150),
                          styleMask: [.titled, .closable, .miniaturizable, .resizable],
                          backing: .buffered, defer: false)
        
        super.init()
        
        window.contentView = view
        window.makeKeyAndOrderFront(nil)
    }
    
    func applicationDidFinishLaunching(_ notification: Notification) {
        NSApp.activate(ignoringOtherApps: true)
    }
}

// Run the application
let appDelegate = AppDelegate()
NSApplication.shared.delegate = appDelegate
NSApplication.shared.run()
