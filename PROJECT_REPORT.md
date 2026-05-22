# 🏛️ Project Report: EduNavigator AI Academic Portal

**Institution**: SRM University AP  
**System Name**: EduNavigator AI  
**Version**: 2.0 (Conversational Update)

---

## 📝 Abstract
EduNavigator AI is an advanced conversational academic workspace designed to bridge the gap between institutional document repositories and student accessibility. By integrating Generative AI (LLMs) with Vector-based Semantic Search, the portal provides an interactive, chat-based interface where students can query both global course materials provided by faculty and session-specific research documents. The system emphasizes persistent session management, contextual memory, and a high-end institutional aesthetic.

---

## 1. Introduction
### 1.1 Background
Modern academic environments deal with vast amounts of digital information (PDFs, research papers, lecture notes). Traditional keyword search often fails to retrieve contextually relevant insights.
### 1.2 Problem Statement
Students struggle to synthesize information from multiple disparate sources quickly, while faculty lack a centralized, intelligent platform to distribute and interactively discuss course materials.
### 1.3 Proposed Solution
A centralized conversational portal that hosts an "AI Brain" capable of understanding, chunking, and discussing academic content in a natural, persistent chat environment.

---

## 2. Methodology
### 2.1 Data Ingestion & Processing
*   **Document Parsing**: Supports PDF and TXT ingestion.
*   **Semantic Chunking**: Documents are broken into contextual blocks for precise retrieval.
*   **Vector Embeddings**: Uses the `all-MiniLM-L6-v2` model to transform text into high-dimensional numerical vectors.

### 2.2 Knowledge Retrieval (RAG)
The system implements **Retrieval-Augmented Generation (RAG)**:
1.  **Query Transformation**: Student questions are embedded into vectors.
2.  **Hybrid Search**: The system performs a similarity search across the MongoDB Vector Index, filtered by both Global (Faculty) and Session (Student) tags.
3.  **Contextual Augmentation**: Relevant chunks are injected into the LLM prompt.

### 2.3 Generative Intelligence
Powered by `Groq Grok` (via Puter integration), the system generates human-like, technically accurate responses based on the retrieved academic context.

---

## 3. Project Architecture
The system follows a **Three-Tier Architecture**:

### 3.1 Presentation Layer (Frontend)
*   **Technologies**: HTML5, CSS3, JavaScript (ES6+).
*   **Design Philosophy**: "Fazal Style" aesthetics utilizing SRMAP branding (Navy/Gold), glassmorphism, and responsive layouts.

### 3.2 Application Layer (Backend)
*   **Framework**: FastAPI (High-performance ASGI framework).
*   **Logic**: Handles JWT Authentication, Chat State Management, and AI Orchestration.

### 3.3 Data Layer (Database)
*   **Storage**: MongoDB Atlas (Cloud NoSQL).
*   **Collections**: `users`, `documents`, `chunks`, `chats`, `query_logs`.

---

## 4. System Requirements
### 4.1 Functional Requirements
*   **User Management**: Secure Login/Register with role-based access (Faculty/Student).
*   **Conversational Chat**: Multi-turn dialogue with session persistence.
*   **Document Interaction**: Temporary session-based file analysis for students.
*   **Global Knowledge Base**: Persistent academic library managed by faculty.
*   **Chat Management**: Functionality to create, rename, and delete chat sessions.

### 4.2 Non-Functional Requirements
*   **Performance**: AI response latency optimized through Groq's fast inference engine.
*   **Scalability**: Stateless backend design allowing horizontal scaling.
*   **Security**: JWT-based tokenization for session security; BCrypt for password hashing.
*   **Aesthetics**: 10/10 Premium institutional UI design.

---

## 5. Conclusion
EduNavigator AI represents a significant leap in academic toolsets at SRM University AP. By combining the power of modern LLMs with institutional data, it creates a secure, intelligent, and highly responsive learning environment for the next generation of scholars.

---
**© 2026 SRM University AP. Intelligent Learning Systems.**
