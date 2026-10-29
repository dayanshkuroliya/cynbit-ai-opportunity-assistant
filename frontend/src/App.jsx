import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const askQuestion = async (customQuestion = null) => {
    const currentQuestion = customQuestion || question;

    if (!currentQuestion.trim() || loading) {
      return;
    }

    setLoading(true);

    setMessages((previousMessages) => [
      ...previousMessages,
      {
        role: "user",
        text: currentQuestion,
      },
    ]);

    setQuestion("");

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: currentQuestion,
        }),
      });

      if (!response.ok) {
        throw new Error("HTTP error: " + response.status);
      }

      const data = await response.json();

      setMessages((previousMessages) => [
        ...previousMessages,
        {
          role: "assistant",
          text: data.answer,
          sources: data.sources || [],
        },
      ]);
    } catch (error) {
      console.error("Chat error:", error);

      setMessages((previousMessages) => [
        ...previousMessages,
        {
          role: "assistant",
          text: "Sorry, I could not connect to the Cynbit AI server.",
          sources: [],
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      askQuestion();
    }
  };

  return (
    <div className="app">
      <div className="chat-container">

        {/* Header */}
        <header className="chat-header">
          <div className="brand-icon">✦</div>

          <div>
            <h1>Cynbit AI</h1>
            <p>AI Opportunity Assistant</p>
          </div>

          <div className="online-status">
            <span></span>
            Online
          </div>
        </header>

        {/* Chat Area */}
        <main className="chat-area">

          {/* Welcome Screen */}
          {messages.length === 0 && (
            <div className="welcome">

              <div className="optimistic-badge">
                <span></span>
                THE OPTIMISTIC ARCHITECT
              </div>

              <div className="welcome-icon">✦</div>

              <h2>
                Explore Cynbit with
                <br />
                <em>AI-powered discovery.</em>
              </h2>

              <p>
                Ask about Cynbit's services, products,
                technologies, internships, careers and
                opportunities.
              </p>

              <div className="suggestions">

                <button
                  onClick={() =>
                    askQuestion("What internships does Cynbit offer?")
                  }
                >
                  What internships does Cynbit offer?
                </button>

                <button
                  onClick={() =>
                    askQuestion("What services does Cynbit provide?")
                  }
                >
                  What services does Cynbit provide?
                </button>

                <button
                  onClick={() =>
                    askQuestion("What technologies does Cynbit use?")
                  }
                >
                  What technologies does Cynbit use?
                </button>

              </div>
            </div>
          )}

          {/* Messages */}
          {messages.map((message, index) => (
            <div
              key={index}
              className={"message-row " + message.role}
            >

              <div className="message-avatar">
                {message.role === "user" ? "You" : "✦"}
              </div>

              <div className="message-content">

                <div className="message-name">
                  {message.role === "user"
                    ? "You"
                    : "Cynbit AI"}
                </div>

                <div className="message-bubble">
                  {message.text}
                </div>

                {/* Sources */}
                {message.role === "assistant" &&
                  message.sources &&
                  message.sources.length > 0 && (
                    <div className="sources">

                      <div className="sources-title">
                        <span>◈</span>
                        Sources used
                      </div>

                      <div className="source-list">

                        {message.sources.map(
                          (source, sourceIndex) => (
                            <div
                              className="source-card"
                              key={sourceIndex}
                            >

                              <div className="source-icon">
                                📄
                              </div>

                              <div className="source-info">

                                <div className="source-file">
                                  {source.file}
                                </div>

                                <div className="source-score">
                                  Relevance:{" "}
                                  {(source.score * 100).toFixed(1)}
                                  %
                                </div>

                              </div>

                            </div>
                          )
                        )}

                      </div>
                    </div>
                  )}

              </div>
            </div>
          ))}

          {/* Loading */}
          {loading && (
            <div className="message-row assistant">

              <div className="message-avatar">
                ✦
              </div>

              <div className="message-content">

                <div className="message-name">
                  Cynbit AI
                </div>

                <div className="loading-bubble">

                  <div className="thinking-icon">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>

                  <span>Thinking...</span>

                </div>

              </div>

            </div>
          )}

        </main>

        {/* Input */}
        <div className="input-area">

          <input
            type="text"
            placeholder="Ask Cynbit AI anything..."
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            onKeyDown={handleKeyDown}
            disabled={loading}
          />

          <button
            className="send-button"
            onClick={() => askQuestion()}
            disabled={loading || !question.trim()}
          >
            {loading ? "..." : "➤"}
          </button>

        </div>

        <div className="footer-text">
          Cynbit AI Assistant • Powered by RAG
        </div>

      </div>
    </div>
  );
}

export default App;