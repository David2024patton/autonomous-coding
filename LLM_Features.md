<project_specification>
  <project_name>Claude.ai Clone - AI Chat Interface</project_name>

  <overview>
    Build a fully functional clone of claude.ai, Anthropic's conversational AI interface. The application should
    provide a clean, modern chat interface for interacting with Claude via the API, including features like
    conversation management, artifact rendering, project organization, multiple model selection, and advanced
    settings. The UI should closely match claude.ai's design using Tailwind CSS with a focus on excellent
    user experience and responsive design.
  </overview>

  <technology_stack>
    <api_key>
        You can use an API key located at /tmp/api-key for testing. You will not be allowed to read this file, but you can reference it in code.
    </api_key>
    <frontend>
      <framework>React with Vite</framework>
      <styling>Tailwind CSS (via CDN)</styling>
      <state_management>React hooks and context</state_management>
      <routing>React Router for navigation</routing>
      <markdown>React Markdown for message rendering</markdown>
      <code_highlighting>Syntax highlighting for code blocks</code_highlighting>
      <port>Only launch on port {frontend_port}</port>
    </frontend>
    <backend>
      <runtime>Node.js with Express</runtime>
      <database>SQLite with better-sqlite3</database>
      <api_integration>Claude API for chat completions</api_integration>
      <streaming>Server-Sent Events for streaming responses</streaming>
    </backend>
    <communication>
      <api>RESTful endpoints</api>
      <streaming>SSE for real-time message streaming</streaming>
      <claude_api>Integration with Claude API using Anthropic SDK</claude_api>
    </communication>
  </technology_stack>

  <prerequisites>
    <environment_setup>
      - Repository includes .env with VITE_ANTHROPIC_API_KEY configured
      - Frontend dependencies pre-installed via pnpm
      - Backend code goes in /server directory
      - Install backend dependencies as needed
    </environment_setup>
  </prerequisites>

  <core_features>
    <chat_interface>
      - Clean, centered chat layout with message bubbles
      - Streaming message responses with typing indicator
      - Markdown rendering with proper formatting
      - Code blocks with syntax highlighting and copy button
      - LaTeX/math equation rendering
      - Image upload and display in messages
      - Multi-turn conversations with context
      - Message editing and regeneration
      - Stop generation button during streaming
      - Input field with auto-resize textarea
      - Character count and token estimation
      - Keyboard shortcuts (Enter to send, Shift+Enter for newline)
    </chat_interface>

    <artifacts>
      - Artifact detection and rendering in side panel
      - Code artifact viewer with syntax highlighting
      - HTML/SVG preview with live rendering
      - React component preview
      - Mermaid diagram rendering
      - Text document artifacts
      - Artifact editing and re-prompting
      - Full-screen artifact view
      - Download artifact content
      - Artifact versioning and history
    </artifacts>

    <conversation_management>
      - Create new conversations
      - Conversation list in sidebar
      - Rename conversations
      - Delete conversations
      - Search conversations by title/content
      - Pin important conversations
      - Archive conversations
      - Conversation folders/organization
      - Duplicate conversation
      - Export conversation (JSON, Markdown, PDF)
      - Conversation timestamps (created, last updated)
      - Unread message indicators
    </conversation_management>

    <projects>
      - Create projects to group related conversations
      - Project knowledge base (upload documents)
      - Project-specific custom instructions
      - Share projects with team (mock feature)
      - Project settings and configuration
      - Move conversations between projects
      - Project templates
      - Project analytics (usage stats)
    </projects>

    <model_selection>
      - Model selector dropdown with the following models:
        - Claude Sonnet 4.5 (claude-sonnet-4-5-20250929) - default
        - Claude Haiku 4.5 (claude-haiku-4-5-20251001)
        - Claude Opus 4.1 (claude-opus-4-1-20250805)
      - Model capabilities display
      - Context window indicator
      - Model-specific pricing info (display only)
      - Switch models mid-conversation
      - Model comparison view
    </model_selection>

    <custom_instructions>
      - Global custom instructions
      - Project-specific custom instructions
      - Conversation-specific system prompts
      - Custom instruction templates
      - Preview how instructions affect responses
    </custom_instructions>

    <settings_preferences>
      - Theme selection (Light, Dark, Auto)
      - Font size adjustment
      - Message density (compact, comfortable, spacious)
      - Code theme selection
      - Language preferences
      - Accessibility options
      - Keyboard shortcuts reference
      - Data export options
      - Privacy settings
      - API key management
    </settings_preferences>

    <advanced_features>
      - Temperature control slider
      - Max tokens adjustment
      - Top-p (nucleus sampling) control
      - System prompt override
      - Thinking/reasoning mode toggle
      - Multi-modal input (text + images)
      - Voice input (optional, mock UI)
      - Response suggestions
      - Related prompts
      - Conversation branching
    </advanced_features>

    <collaboration>
      - Share conversation via link (read-only)
      - Export conversation formats
      - Conversation templates
      - Prompt library
      - Share artifacts
      - Team workspaces (mock UI)
    </collaboration>

    <search_discovery>
      - Search across all conversations
      - Filter by project, date, model
      - Prompt library with categories
      - Example conversations
      - Quick actions menu
      - Command palette (Cmd/Ctrl+K)
    </search_discovery>

    <usage_tracking>
      - Token usage display per message
      - Conversation cost estimation
      - Daily/monthly usage dashboard
      - Usage limits and warnings
      - API quota tracking
    </usage_tracking>

    <onboarding>
      - Welcome screen for new users
      - Feature tour highlights
      - Example prompts to get started
      - Quick tips and best practices
      - Keyboard shortcuts tutorial
    </onboarding>

    <accessibility>
      - Full keyboard navigation
      - Screen reader support
      - ARIA labels and roles
      - High contrast mode
      - Focus management
      - Reduced motion support
    </accessibility>

    <responsive_design>
      - Mobile-first responsive layout
      - Touch-optimized interface
      - Collapsible sidebar on mobile
      - Swipe gestures for navigation
      - Adaptive artifact display
      - Progressive Web App (PWA) support
    </responsive_design>
  </core_features>

  <database_schema>
    <tables>
      <users>
        - id, email, name, avatar_url
        - created_at, last_login
        - preferences (JSON: theme, font_size, etc.)
        - custom_instructions
      </users>

      <projects>
        - id, user_id, name, description, color
        - custom_instructions, knowledge_base_path
        - created_at, updated_at
        - is_archived, is_pinned
      </projects>

      <conversations>
        - id, user_id, project_id, title
        - model, created_at, updated_at, last_message_at
        - is_archived, is_pinned, is_deleted
        - settings (JSON: temperature, max_tokens, etc.)
        - token_count, message_count
      </conversations>

      <messages>
        - id, conversation_id, role (user/assistant/system)
        - content, created_at, edited_at
        - tokens, finish_reason
        - images (JSON array of image data)
        - parent_message_id (for branching)
      </messages>

      <artifacts>
        - id, message_id, conversation_id
        - type (code/html/svg/react/mermaid/text)
        - title, identifier, language
        - content, version
        - created_at, updated_at
      </artifacts>

      <shared_conversations>
        - id, conversation_id, share_token
        - created_at, expires_at, view_count
        - is_public
      </shared_conversations>

      <prompt_library>
        - id, user_id, title, description
        - prompt_template, category, tags (JSON)
        - is_public, usage_count
        - created_at, updated_at
      </prompt_library>

      <conversation_folders>
        - id, user_id, project_id, name, parent_folder_id
        - created_at, position
      </conversation_folders>

      <conversation_folder_items>
        - id, folder_id, conversation_id
      </conversation_folder_items>

      <usage_tracking>
        - id, user_id, conversation_id, message_id
        - model, input_tokens, output_tokens
        - cost_estimate, created_at
      </usage_tracking>

      <api_keys>
        - id, user_id, key_name, api_key_hash
        - created_at, last_used_at
        - is_active
      </api_keys>
    </tables>
  </database_schema>

  <api_endpoints_summary>
    <authentication>
      - POST /api/auth/login
      - POST /api/auth/logout
      - GET /api/auth/me
      - PUT /api/auth/profile
    </authentication>

    <conversations>
      - GET /api/conversations
      - POST /api/conversations
      - GET /api/conversations/:id
      - PUT /api/conversations/:id
      - DELETE /api/conversations/:id
      - POST /api/conversations/:id/duplicate
      - POST /api/conversations/:id/export
      - PUT /api/conversations/:id/archive
      - PUT /api/conversations/:id/pin
      - POST /api/conversations/:id/branch
    </conversations>

    <messages>
      - GET /api/conversations/:id/messages
      - POST /api/conversations/:id/messages
      - PUT /api/messages/:id
      - DELETE /api/messages/:id
      - POST /api/messages/:id/regenerate
      - GET /api/messages/stream (SSE endpoint)
    </messages>

    <artifacts>
      - GET /api/conversations/:id/artifacts
      - GET /api/artifacts/:id
      - PUT /api/artifacts/:id
      - DELETE /api/artifacts/:id
      - POST /api/artifacts/:id/fork
      - GET /api/artifacts/:id/versions
    </artifacts>

    <projects>
      - GET /api/projects
      - POST /api/projects
      - GET /api/projects/:id
      - PUT /api/projects/:id
      - DELETE /api/projects/:id
      - POST /api/projects/:id/knowledge
      - GET /api/projects/:id/conversations
      - PUT /api/projects/:id/settings
    </projects>

    <sharing>
      - POST /api/conversations/:id/share
      - GET /api/share/:token
      - DELETE /api/share/:token
      - PUT /api/share/:token/settings
    </sharing>

    <prompts>
      - GET /api/prompts/library
      - POST /api/prompts/library
      - GET /api/prompts/:id
      - PUT /api/prompts/:id
      - DELETE /api/prompts/:id
      - GET /api/prompts/categories
      - GET /api/prompts/examples
    </prompts>

    <search>
      - GET /api/search/conversations?q=query
      - GET /api/search/messages?q=query
      - GET /api/search/artifacts?q=query
      - GET /api/search/prompts?q=query
    </search>

    <folders>
      - GET /api/folders
      - POST /api/folders
      - PUT /api/folders/:id
      - DELETE /api/folders/:id
      - POST /api/folders/:id/items
      - DELETE /api/folders/:id/items/:conversationId
    </folders>

    <usage>
      - GET /api/usage/daily
      - GET /api/usage/monthly
      - GET /api/usage/by-model
      - GET /api/usage/conversations/:id
    </usage>

    <settings>
      - GET /api/settings
      - PUT /api/settings
      - GET /api/settings/custom-instructions
      - PUT /api/settings/custom-instructions
    </settings>

    <claude_api>
      - POST /api/claude/chat (proxy to Claude API)
      - POST /api/claude/chat/stream (streaming proxy)
      - GET /api/claude/models
      - POST /api/claude/images/upload
    </claude_api>
  </api_endpoints_summary>

  <ui_layout>
    <main_structure>
      - Three-column layout: sidebar (conversations), main (chat), panel (artifacts)
      - Collapsible sidebar with resize handle
      - Responsive breakpoints: mobile (single column), tablet (two column), desktop (three column)
      - Persistent header with project/model selector
      - Bottom input area with send button and options
    </main_structure>

    <sidebar_left>
      - New chat button (prominent)
      - Project selector dropdown
      - Search conversations input
      - Conversations list (grouped by date: Today, Yesterday, Previous 7 days, etc.)
      - Folder tree view (collapsible)
      - Settings gear icon at bottom
      - User profile at bottom
    </sidebar_left>

    <main_chat_area>
      - Conversation title (editable inline)
      - Model selector badge
      - Message history (scrollable)
      - Welcome screen for new conversations
      - Suggested prompts (empty state)
      - Input area with formatting toolbar
      - Attachment button for images
      - Send button with loading state
      - Stop generation button
    </main_chat_area>

    <artifacts_panel>
      - Artifact header with title and type badge
      - Code editor or preview pane
      - Tabs for multiple artifacts
      - Full-screen toggle
      - Download button
      - Edit/Re-prompt button
      - Version selector
      - Close panel button
    </artifacts_panel>

    <modals_overlays>
      - Settings modal (tabbed interface)
      - Share conversation modal
      - Export options modal
      - Project settings modal
      - Prompt library modal
      - Command palette overlay
      - Keyboard shortcuts reference
    </modals_overlays>
  </ui_layout>

  <design_system>
    <color_palette>
      - Primary: Orange/amber accent (#CC785C claude-style)
      - Background: White (light mode), Dark gray (#1A1A1A dark mode)
      - Surface: Light gray (#F5F5F5 light), Darker gray (#2A2A2A dark)
      - Text: Near black (#1A1A1A light), Off-white (#E5E5E5 dark)
      - Borders: Light gray (#E5E5E5 light), Dark gray (#404040 dark)
      - Code blocks: Monaco editor theme
    </color_palette>

    <typography>
      - Sans-serif system font stack (Inter, SF Pro, Roboto, system-ui)
      - Headings: font-semibold
      - Body: font-normal, leading-relaxed
      - Code: Monospace (JetBrains Mono, Consolas, Monaco)
      - Message text: text-base (16px), comfortable line-height
    </typography>

    <components>
      <message_bubble>
        - User messages: Right-aligned, subtle background
        - Assistant messages: Left-aligned, no background
        - Markdown formatting with proper spacing
        - Inline code with bg-gray-100 background
        - Code blocks with syntax highlighting
        - Copy button on code blocks
      </message_bubble>

      <buttons>
        - Primary: Orange/amber background, white text, rounded
        - Secondary: Border style with hover fill
        - Icon buttons: Square with hover background
        - Disabled state: Reduced opacity, no pointer events
      </buttons>

      <inputs>
        - Rounded borders with focus ring
        - Textarea auto-resize
        - Placeholder text in gray
        - Error states in red
        - Character counter
      </inputs>

      <cards>
        - Subtle border or shadow
        - Rounded corners (8px)
        - Padding: p-4 to p-6
        - Hover state: slight shadow increase
      </cards>
    </components>

    <animations>
      - Smooth transitions (150-300ms)
      - Fade in for new messages
      - Slide in for sidebar
      - Typing indicator animation
      - Loading spinner for generation
      - Skeleton loaders for content
    </animations>
  </design_system>

  <key_interactions>
    <message_flow>
      1. User types message in input field
      2. Optional: Attach images via button
      3. Click send or press Enter
      4. Message appears in chat immediately
      5. Typing indicator shows while waiting
      6. Response streams in word by word
      7. Code blocks render with syntax highlighting
      8. Artifacts detected and rendered in side panel
      9. Message complete, enable regenerate option
    </message_flow>

    <artifact_flow>
      1. Assistant generates artifact in response
      2. Artifact panel slides in from right
      3. Content renders (code with highlighting or live preview)
      4. User can edit artifact inline
      5. "Re-prompt" button to iterate with Claude
      6. Download or copy artifact content
      7. Full-screen mode for detailed work
      8. Close panel to return to chat focus
    </artifact_flow>

    <conversation_management>
      1. Click "New Chat" to start fresh conversation
      2. Conversations auto-save with first message
      3. Auto-generate title from first exchange
      4. Click title to rename inline
      5. Drag conversations into folders
      6. Right-click for context menu (pin, archive, delete, export)
      7. Search filters conversations in real-time
      8. Click conversation to switch context
    </conversation_management>
  </key_interactions>

  <implementation_steps>
    <step number="1">
      <title>Setup Project Foundation and Database</title>
      <tasks>
        - Initialize Express server with SQLite database
        - Set up Claude API client with streaming support
        - Create database schema with migrations
        - Implement authentication endpoints
        - Set up basic CORS and middleware
        - Create health check endpoint
      </tasks>
    </step>

    <step number="2">
      <title>Build Core Chat Interface</title>
      <tasks>
        - Create main layout with sidebar and chat area
        - Implement message display with markdown rendering
        - Add streaming message support with SSE
        - Build input area with auto-resize textarea
        - Add code block syntax highlighting
        - Implement stop generation functionality
        - Add typing indicators and loading states
      </tasks>
    </step>

    <step number="3">
      <title>Conversation Management</title>
      <tasks>
        - Create conversation list in sidebar
        - Implement new conversation creation
        - Add conversation switching
        - Build conversation rename functionality
        - Implement delete with confirmation
        - Add conversation search
        - Create conversation grouping by date
      </tasks>
    </step>

    <step number="4">
      <title>Artifacts System</title>
      <tasks>
        - Build artifact detection from Claude responses
        - Create artifact rendering panel
        - Implement code artifact viewer
        - Add HTML/SVG live preview
        - Build artifact editing interface
        - Add artifact versioning
        - Implement full-screen artifact view
      </tasks>
    </step>

    <step number="5">
      <title>Projects and Organization</title>
      <tasks>
        - Create projects CRUD endpoints
        - Build project selector UI
        - Implement project-specific custom instructions
        - Add folder system for conversations
        - Create drag-and-drop organization
        - Build project settings panel
      </tasks>
    </step>

    <step number="6">
      <title>Advanced Features</title>
      <tasks>
        - Add model selection dropdown
        - Implement temperature and parameter controls
        - Build image upload functionality
        - Create message editing and regeneration
        - Add conversation branching
        - Implement export functionality
      </tasks>
    </step>

    <step number="7">
      <title>Settings and Customization</title>
      <tasks>
        - Build settings modal with tabs
        - Implement theme switching (light/dark)
        - Add custom instructions management
        - Create keyboard shortcuts
        - Build prompt library
        - Add usage tracking dashboard
      </tasks>
    </step>

    <step number="8">
      <title>Sharing and Collaboration</title>
      <tasks>
        - Implement conversation sharing with tokens
        - Create public share view
        - Add export to multiple formats
        - Build prompt templates
        - Create example conversations
      </tasks>
    </step>

    <step number="9">
      <title>Polish and Optimization</title>
      <tasks>
        - Optimize for mobile responsiveness
        - Add command palette (Cmd+K)
        - Implement comprehensive keyboard navigation
        - Add onboarding flow
        - Create accessibility improvements
        - Performance optimization and caching
      </tasks>
    </step>
  </implementation_steps>

  <success_criteria>
    <functionality>
      - Streaming chat responses work smoothly
      - Artifact detection and rendering accurate
      - Conversation management intuitive and reliable
      - Project organization clear and useful
      - Image upload and display working
      - All CRUD operations functional
    </functionality>

    <user_experience>
      - Interface matches claude.ai design language
      - Responsive on all device sizes
      - Smooth animations and transitions
      - Fast response times and minimal lag
      - Intuitive navigation and workflows
      - Clear feedback for all actions
    </user_experience>

    <technical_quality>
      - Clean, maintainable code structure
      - Proper error handling throughout
      - Secure API key management
      - Optimized database queries
      - Efficient streaming implementation
      - Comprehensive testing coverage
    </technical_quality>

    <design_polish>
      - Consistent with claude.ai visual design
      - Beautiful typography and spacing
      - Smooth animations and micro-interactions
      - Excellent contrast and accessibility
      - Professional, polished appearance
      - Dark mode fully implemented
    </design_polish>
  </success_criteria>
</project_specification>




## YOUR ROLE - CODING AGENT

You are continuing work on a long-running autonomous development task.
This is a FRESH context window - you have no memory of previous sessions.

### STEP 1: GET YOUR BEARINGS (MANDATORY)

Start by orienting yourself:

```bash
# 1. See your working directory
pwd

# 2. List files to understand project structure
ls -la

# 3. Read the project specification to understand what you're building
cat app_spec.txt

# 4. Read the feature list to see all work
cat feature_list.json | head -50

# 5. Read progress notes from previous sessions
cat claude-progress.txt

# 6. Check recent git history
git log --oneline -20

# 7. Count remaining tests
cat feature_list.json | grep '"passes": false' | wc -l
```

Understanding the `app_spec.txt` is critical - it contains the full requirements
for the application you're building.

### STEP 2: START SERVERS (IF NOT RUNNING)

If `init.sh` exists, run it:
```bash
chmod +x init.sh
./init.sh
```

Otherwise, start servers manually and document the process.

### STEP 3: VERIFICATION TEST (CRITICAL!)

**MANDATORY BEFORE NEW WORK:**

The previous session may have introduced bugs. Before implementing anything
new, you MUST run verification tests.

Run 1-2 of the feature tests marked as `"passes": true` that are most core to the app's functionality to verify they still work.
For example, if this were a chat app, you should perform a test that logs into the app, sends a message, and gets a response.

**If you find ANY issues (functional or visual):**
- Mark that feature as "passes": false immediately
- Add issues to a list
- Fix all issues BEFORE moving to new features
- This includes UI bugs like:
  * White-on-white text or poor contrast
  * Random characters displayed
  * Incorrect timestamps
  * Layout issues or overflow
  * Buttons too close together
  * Missing hover states
  * Console errors

### STEP 4: CHOOSE ONE FEATURE TO IMPLEMENT

Look at feature_list.json and find the highest-priority feature with "passes": false.

Focus on completing one feature perfectly and completing its testing steps in this session before moving on to other features.
It's ok if you only complete one feature in this session, as there will be more sessions later that continue to make progress.

### STEP 5: IMPLEMENT THE FEATURE

Implement the chosen feature thoroughly:
1. Write the code (frontend and/or backend as needed)
2. Test manually using browser automation (see Step 6)
3. Fix any issues discovered
4. Verify the feature works end-to-end

### STEP 6: VERIFY WITH BROWSER AUTOMATION

**CRITICAL:** You MUST verify features through the actual UI.

Use browser automation tools:
- Navigate to the app in a real browser
- Interact like a human user (click, type, scroll)
- Take screenshots at each step
- Verify both functionality AND visual appearance

**DO:**
- Test through the UI with clicks and keyboard input
- Take screenshots to verify visual appearance
- Check for console errors in browser
- Verify complete user workflows end-to-end

**DON'T:**
- Only test with curl commands (backend testing alone is insufficient)
- Use JavaScript evaluation to bypass UI (no shortcuts)
- Skip visual verification
- Mark tests passing without thorough verification

### STEP 7: UPDATE feature_list.json (CAREFULLY!)

**YOU CAN ONLY MODIFY ONE FIELD: "passes"**

After thorough verification, change:
```json
"passes": false
```
to:
```json
"passes": true
```

**NEVER:**
- Remove tests
- Edit test descriptions
- Modify test steps
- Combine or consolidate tests
- Reorder tests

**ONLY CHANGE "passes" FIELD AFTER VERIFICATION WITH SCREENSHOTS.**

### STEP 8: COMMIT YOUR PROGRESS

Make a descriptive git commit:
```bash
git add .
git commit -m "Implement [feature name] - verified end-to-end

- Added [specific changes]
- Tested with browser automation
- Updated feature_list.json: marked test #X as passing
- Screenshots in verification/ directory
"
```

### STEP 9: UPDATE PROGRESS NOTES

Update `claude-progress.txt` with:
- What you accomplished this session
- Which test(s) you completed
- Any issues discovered or fixed
- What should be worked on next
- Current completion status (e.g., "45/200 tests passing")

### STEP 10: END SESSION CLEANLY

Before context fills up:
1. Commit all working code
2. Update claude-progress.txt
3. Update feature_list.json if tests verified
4. Ensure no uncommitted changes
5. Leave app in working state (no broken features)

---

## TESTING REQUIREMENTS

**ALL testing must use browser automation tools.**

Available tools:
- puppeteer_navigate - Start browser and go to URL
- puppeteer_screenshot - Capture screenshot
- puppeteer_click - Click elements
- puppeteer_fill - Fill form inputs
- puppeteer_evaluate - Execute JavaScript (use sparingly, only for debugging)

Test like a human user with mouse and keyboard. Don't take shortcuts by using JavaScript evaluation.
Don't use the puppeteer "active tab" tool.

---

## IMPORTANT REMINDERS

**Your Goal:** Production-quality application with all 200+ tests passing

**This Session's Goal:** Complete at least one feature perfectly

**Priority:** Fix broken tests before implementing new features

**Quality Bar:**
- Zero console errors
- Polished UI matching the design specified in app_spec.txt
- All features work end-to-end through the UI
- Fast, responsive, professional

**You have unlimited time.** Take as long as needed to get it right. The most important thing is that you
leave the code base in a clean state before terminating the session (Step 10).

---

Begin by running Step 1 (Get Your Bearings).




## YOUR ROLE - INITIALIZER AGENT (Session 1 of Many)

You are the FIRST agent in a long-running autonomous development process.
Your job is to set up the foundation for all future coding agents.

### FIRST: Read the Project Specification

Start by reading `app_spec.txt` in your working directory. This file contains
the complete specification for what you need to build. Read it carefully
before proceeding.

### CRITICAL FIRST TASK: Create feature_list.json

Based on `app_spec.txt`, create a file called `feature_list.json` with 200 detailed
end-to-end test cases. This file is the single source of truth for what
needs to be built.

**Format:**
```json
[
  {
    "category": "functional",
    "description": "Brief description of the feature and what this test verifies",
    "steps": [
      "Step 1: Navigate to relevant page",
      "Step 2: Perform action",
      "Step 3: Verify expected result"
    ],
    "passes": false
  },
  {
    "category": "style",
    "description": "Brief description of UI/UX requirement",
    "steps": [
      "Step 1: Navigate to page",
      "Step 2: Take screenshot",
      "Step 3: Verify visual requirements"
    ],
    "passes": false
  }
]
```

**Requirements for feature_list.json:**
- Minimum 200 features total with testing steps for each
- Both "functional" and "style" categories
- Mix of narrow tests (2-5 steps) and comprehensive tests (10+ steps)
- At least 25 tests MUST have 10+ steps each
- Order features by priority: fundamental features first
- ALL tests start with "passes": false
- Cover every feature in the spec exhaustively

**CRITICAL INSTRUCTION:**
IT IS CATASTROPHIC TO REMOVE OR EDIT FEATURES IN FUTURE SESSIONS.
Features can ONLY be marked as passing (change "passes": false to "passes": true).
Never remove features, never edit descriptions, never modify testing steps.
This ensures no functionality is missed.

### SECOND TASK: Create init.sh

Create a script called `init.sh` that future agents can use to quickly
set up and run the development environment. The script should:

1. Install any required dependencies
2. Start any necessary servers or services
3. Print helpful information about how to access the running application

Base the script on the technology stack specified in `app_spec.txt`.

### THIRD TASK: Initialize Git

Create a git repository and make your first commit with:
- feature_list.json (complete with all 200+ features)
- init.sh (environment setup script)
- README.md (project overview and setup instructions)

Commit message: "Initial setup: feature_list.json, init.sh, and project structure"

### FOURTH TASK: Create Project Structure

Set up the basic project structure based on what's specified in `app_spec.txt`.
This typically includes directories for frontend, backend, and any other
components mentioned in the spec.

### OPTIONAL: Start Implementation

If you have time remaining in this session, you may begin implementing
the highest-priority features from feature_list.json. Remember:
- Work on ONE feature at a time
- Test thoroughly before marking "passes": true
- Commit your progress before session ends

### ENDING THIS SESSION

Before your context fills up:
1. Commit all work with descriptive messages
2. Create `claude-progress.txt` with a summary of what you accomplished
3. Ensure feature_list.json is complete and saved
4. Leave the environment in a clean, working state

The next agent will continue from here with a fresh context window.

---

**Remember:** You have unlimited time across many sessions. Focus on
quality over speed. Production-ready is the goal.


Also add all of these features if they arnt in it already 



SkSkip to main content

Open WebUI
Blog
GitHub
Discord

Search Ctrl+K
🏡 Home
🚀 Getting Started

⭐ Features

Federated Authentication

Role-Based Access Control (RBAC)

Retrieval Augmented Generation (RAG)

Tools & Functions (Plugins)

Create & Edit Images

Speech-to-Text & Text-to-Speech

Web Search

Workspace

Chat Features

Interface

Channels
Evaluation
Model Context Protocol (MCP)
Notes
Pipelines

🛠️ Troubleshooting

🏢 Open WebUI for Enterprises

🎓 Tutorials

❓ FAQ
🛣️ Roadmap
🛡️ Security Policy
🤝 Contributing
💖 Sponsorships
🎨 Design Guidelines
⚖️ Open WebUI License
🎯 Our Mission
👥 Our Team
Sponsored by Open WebUI Inc.
Open WebUI Inc.
We are hiring! Shape the way humanity engages with intelligence.

⭐ Features
Sponsored by Open WebUI Inc.
Open WebUI Inc.
We are hiring! Shape the way humanity engages with intelligence.

Key Features of Open WebUI ⭐
🚀 Effortless Setup: Install seamlessly using Docker, Kubernetes, Podman, Helm Charts (kubectl, kustomize, podman, or helm) for a hassle-free experience with support for both :ollama image with bundled Ollama and :cuda with CUDA support.

🛠️ Guided Initial Setup: Complete the setup process with clarity, including an explicit indication of creating an admin account during the first-time setup.

🤝 OpenAI API Integration: Effortlessly integrate OpenAI-compatible APIs for versatile conversations alongside Ollama models. The OpenAI API URL can be customized to integrate Open WebUI seamlessly with various third-party applications.

🛡️ Granular Permissions and User Groups: By allowing administrators to create detailed user roles, user groups, and permissions across the workspace, we ensure a secure user environment for all users involved. This granularity not only enhances security, but also allows for customized user experiences, fostering a sense of ownership and responsibility amongst users.

🔐 SCIM 2.0 Provisioning: Enterprise-grade user and group provisioning through SCIM 2.0 protocol, enabling seamless integration with identity providers like Okta, Azure AD, and Google Workspace for automated user lifecycle management.

📱 Responsive Design: Enjoy a seamless experience across desktop PCs, laptops, and mobile devices.

📱 Progressive Web App for Mobile: Enjoy a native progressive web application experience on your mobile device with offline access on localhost or a personal domain, and a smooth user interface. In order for our PWA to be installable on your device, it must be delivered in a secure context. This usually means that it must be served over HTTPS.

info
To set up a PWA, you'll need some understanding of technologies like Linux, Docker, and reverse proxies such as Nginx, Caddy, or Traefik. Using these tools can help streamline the process of building and deploying a PWA tailored to your needs. While there's no "one-click install" option available, and your available option to securely deploy your Open WebUI instance over HTTPS requires user experience, using these resources can make it easier to create and deploy a PWA tailored to your needs.
✒️🔢 Full Markdown and LaTeX Support: Elevate your LLM experience with comprehensive Markdown, LaTex, and Rich Text capabilities for enriched interaction.

🧩 Model Builder: Easily create custom models from base Ollama models directly from Open WebUI. Create and add custom characters and agents, customize model elements, and import models effortlessly through Open WebUI Community integration.

📚 Advanced RAG Integration with Multiple Vector Databases: Dive into the future of chat interactions with cutting-edge Retrieval Augmented Generation (RAG) technology. Choose from 9 vector database options: ChromaDB (default), PostgreSQL with PGVector, Qdrant, Milvus, Elasticsearch, OpenSearch, Pinecone, S3Vector, and Oracle 23ai. Documents can be loaded into the Documents tab of the Workspace and accessed using the pound key [#] before a query, or by starting the prompt with [#] followed by a URL for webpage content integration.

📄 Advanced Document Extraction with Multiple Engines: Extract text and data from various document formats including PDFs, Word documents, Excel spreadsheets, PowerPoint presentations, and more using your choice of extraction engines: Apache Tika, Docling, Azure Document Intelligence, Mistral OCR, or external custom (self-built) content extraction engines/document loaders. Advanced document processing capabilities enable seamless integration with your knowledge base, preserving structure and formatting while supporting OCR for scanned documents and images.

🔍 Web Search for RAG with 15+ Providers: Perform web searches using 15+ providers including SearXNG, Google PSE, Brave Search, Kagi, Mojeek, Bocha, Tavily, Perplexity (AI models and Search API), serpstack, serper, Serply, DuckDuckGo, SearchAPI, SerpApi, Bing, Jina, Exa, Sougou, Azure AI Search, and Ollama Cloud, injecting results directly into your local Retrieval Augmented Generation (RAG) experience.

🌐 Web Browsing Capabilities: Integrate websites seamlessly into your chat experience by using the # command followed by a URL. This feature enables the incorporation of web content directly into your conversations, thereby enhancing the richness and depth of your interactions.

🎨 Image Generation & Editing Integration: Seamlessly create and edit images using multiple engines including OpenAI's DALL-E (generation and editing), Gemini (generation and editing), ComfyUI (local, generation and editing), and AUTOMATIC1111 (local, generation). Support for both text-to-image generation and prompt-based image editing workflows with dynamic visual content.

⚙️ Concurrent Model Utilization: Effortlessly engage with multiple models simultaneously, harnessing their unique strengths for optimal responses. Leverage a diverse set of model modalities in parallel to enhance your experience.

🔐 Role-Based Access Control (RBAC): Ensure secure access with restricted permissions. Only authorized individuals can access your Ollama, while model creation and pulling rights are exclusively reserved for administrators.

🌐🌍 Multilingual Support: Experience Open WebUI in your preferred language with our internationalization (i18n) support. We invite you to join us in expanding our supported languages! We're actively seeking contributors!

💾 Persistent Artifact Storage: Built-in key-value storage API for artifacts, enabling features like journals, trackers, leaderboards, and collaborative tools with both personal and shared data scopes that persist across sessions.

☁️ Cloud Storage Integration: Native support for cloud storage backends including Amazon S3 (with S3-compatible providers), Google Cloud Storage, and Microsoft Azure Blob Storage for scalable file storage and data management.

☁️ Enterprise Cloud Integration: Seamlessly import documents from Google Drive and OneDrive/SharePoint directly through the file picker interface, enabling smooth workflows with enterprise cloud storage solutions.

📊 Production Observability with OpenTelemetry: Built-in OpenTelemetry support for comprehensive monitoring with traces, metrics, and logs export to your existing observability stack (Prometheus, Grafana, Jaeger, etc.), enabling production-grade monitoring and debugging.

🔒 Encrypted Database Support: Optional at-rest encryption for SQLite databases using SQLCipher, providing enhanced security for sensitive data in smaller deployments without requiring PostgreSQL infrastructure.

⚖️ Horizontal Scalability for Production: Redis-backed session management and WebSocket support enabling multi-worker and multi-node deployments behind load balancers for high-availability production environments.

🌟 Continuous Updates: We are committed to improving Open WebUI with regular updates, fixes, and new features.

And many more remarkable features including... ⚡️
🔧 Pipelines Support
🔧 Pipelines Framework: Seamlessly integrate and customize your Open WebUI experience with our modular plugin framework for enhanced customization and functionality (https://github.com/open-webui/pipelines). Our framework allows for the easy addition of custom logic and integration of Python libraries, from AI agents to home automation APIs.

📥 Upload Pipeline: Pipelines can be uploaded directly from the Admin Panel > Settings > Pipelines menu, streamlining the pipeline management process.

The possibilities with our Pipelines framework knows no bounds and are practically limitless. Start with a few pre-built pipelines to help you get started!
🔗 Function Calling: Integrate Function Calling seamlessly through Pipelines to enhance your LLM interactions with advanced function calling capabilities.

📚 Custom RAG: Integrate a custom Retrieval Augmented Generation (RAG) pipeline seamlessly to enhance your LLM interactions with custom RAG logic.

📊 Message Monitoring with Langfuse: Monitor and analyze message interactions in real-time usage statistics via Langfuse pipeline.

⚖️ User Rate Limiting: Manage API usage efficiently by controlling the flow of requests sent to LLMs to prevent exceeding rate limits with Rate Limit pipeline.

🌍 Real-Time LibreTranslate Translation: Integrate real-time translations into your LLM interactions using LibreTranslate pipeline, enabling cross-lingual communication.

Please note that this pipeline requires further setup with LibreTranslate in a Docker container to work.
🛡️ Toxic Message Filtering: Our Detoxify pipeline automatically filters out toxic messages to maintain a clean and safe chat environment.

🔒 LLM-Guard: Ensure secure LLM interactions with LLM-Guard pipeline, featuring a Prompt Injection Scanner that detects and mitigates crafty input manipulations targeting large language models. This protects your LLMs from data leakage and adds a layer of resistance against prompt injection attacks.

🕒 Conversation Turn Limits: Improve interaction management by setting limits on conversation turns with Conversation Turn Limit pipeline.

📈 OpenAI Generation Stats: Our OpenAI pipeline provides detailed generation statistics for OpenAI models.

🚀 Multi-Model Support: Our seamless integration with various AI models from various providers expands your possibilities with a wide range of language models to select from and interact with.

In addition to the extensive features and customization options, we also provide a library of example pipelines ready to use along with a practical example scaffold pipeline to help you get started. These resources will streamline your development process and enable you to quickly create powerful LLM interactions using Pipelines and Python. Happy coding! 💡
🖥️ User Experience
🖥️ Intuitive Interface: The chat interface has been designed with the user in mind, drawing inspiration from the user interface of ChatGPT.

⚡ Swift Responsiveness: Enjoy reliably fast and responsive performance.

🎨 Splash Screen: A simple loading splash screen for a smoother user experience.

🌐 Personalized Interface: Choose between a freshly designed search landing page and the classic chat UI from Settings > Interface, allowing for a tailored experience.

📦 Pip Install Method: Installation of Open WebUI can be accomplished via the command pip install open-webui, which streamlines the process and makes it more accessible to new users. For further information, please visit: https://pypi.org/project/open-webui/.

🌈 Theme Customization: Personalize your Open WebUI experience with a range of options, including a variety of solid, yet sleek themes, customizable chat background images, and three mode options: Light, Dark, or OLED Dark mode - or let Her choose for you! ;)

🖼️ Custom Background Support: Set a custom background from Settings > Interface to personalize your experience.

📝 Rich Banners with Markdown: Create visually engaging announcements with markdown support in banners, enabling richer and more dynamic content.

💻 Code Syntax Highlighting: Our syntax highlighting feature enhances code readability, providing a clear and concise view of your code.

🗨️ Markdown Rendering in User Messages: User messages are now rendered in Markdown, enhancing readability and interaction.

🎨 Flexible Text Input Options: Switch between rich text input and legacy text area input for chat, catering to user preferences and providing a choice between advanced formatting and simpler text input.

👆 Effortless Code Sharing : Streamline the sharing and collaboration process with convenient code copying options, including a floating copy button in code blocks and click-to-copy functionality from code spans, saving time and reducing frustration.

🎨 Interactive Artifacts: Render web content and SVGs directly in the interface, supporting quick iterations and live changes for enhanced creativity and productivity.

🖊️ Live Code Editing: Supercharged code blocks allow live editing directly in the LLM response, with live reloads supported by artifacts, streamlining coding and testing.

🔍 Enhanced SVG Interaction: Pan and zoom capabilities for SVG images, including Mermaid diagrams, enable deeper exploration and understanding of complex concepts.

🔍 Text Select Quick Actions: Floating buttons appear when text is highlighted in LLM responses, offering deeper interactions like "Ask a Question" or "Explain", and enhancing overall user experience.

↕️ Bi-Directional Chat Support: You can easily switch between left-to-right and right-to-left chat directions to accommodate various language preferences.

📱 Mobile Accessibility: The sidebar can be opened and closed on mobile devices with a simple swipe gesture.

🤳 Haptic Feedback on Supported Devices: Android devices support haptic feedback for an immersive tactile experience during certain interactions.

🔍 User Settings Search: Quickly search for settings fields, improving ease of use and navigation.

📜 Offline Swagger Documentation: Access developer-friendly Swagger API documentation offline, ensuring full accessibility wherever you are.

💾 Performance Optimizations: Lazy loading of large dependencies minimizes initial memory usage, boosting performance and reducing loading times.

🚀 Persistent and Scalable Configuration: Open WebUI configurations are stored in a database (webui.db), allowing for seamless load balancing, high-availability setups, and persistent settings across multiple instances, making it easy to access and reuse your configurations.

🔄 Portable Import/Export: Easily import and export Open WebUI configurations, simplifying the process of replicating settings across multiple systems.

❓ Quick Access to Documentation & Shortcuts: The question mark button located at the bottom right-hand corner of the main UI screen (available on larger screens like desktop PCs and laptops) provides users with easy access to the Open WebUI documentation page and available keyboard shortcuts.

📜 Changelog & Check for Updates: Users can access a comprehensive changelog and check for updates in the Settings > About > See What's New menu, which provides a quick overview of the latest features, improvements, and bug fixes, as well as the ability to check for updates.

💬 Conversations
💬 True Asynchronous Chat: Enjoy uninterrupted multitasking with true asynchronous chat support, allowing you to create chats, navigate away, and return anytime with responses ready.

🔔 Chat Completion Notifications: Stay updated with instant in-UI notifications when a chat finishes in a non-active tab, ensuring you never miss a completed response.

🌐 Notification Webhook Integration: Receive timely updates for long-running chats or external integration needs with configurable webhook notifications, even when your tab is closed.

📚 Channels (Beta): Explore real-time collaboration between users and AIs with Discord/Slack-style chat rooms, build bots for channels, and unlock asynchronous communication for proactive multi-agent workflows.

🖊️ Typing Indicators in Channels: Enhance collaboration with real-time typing indicators in channels, keeping everyone engaged and informed.

👤 User Status Indicators: Quickly view a user's status by clicking their profile image in channels, providing better coordination and availability insights.

💬 Chat Controls: Easily adjust parameters for each chat session, offering more precise control over your interactions.

💖 Favorite Response Management: Easily mark and organize favorite responses directly from the chat overview, enhancing ease of retrieval and access to preferred responses.

📌 Pinned Chats: Support for pinned chats, allowing you to keep important conversations easily accessible.

🔍 RAG Embedding Support: Change the Retrieval Augmented Generation (RAG) embedding model directly in the Admin Panel > Settings > Documents menu, enhancing document processing. This feature supports Ollama and OpenAI models.

📜 Citations in RAG Feature: The Retrieval Augmented Generation (RAG) feature allows users to easily track the context of documents fed to LLMs with added citations for reference points.

🌟 Enhanced RAG Pipeline: A togglable hybrid search sub-feature for our RAG embedding feature that enhances the RAG functionality via BM25, with re-ranking powered by CrossEncoder, and configurable relevance score thresholds.

📹 YouTube RAG Pipeline: The dedicated Retrieval Augmented Generation (RAG) pipeline for summarizing YouTube videos via video URLs enables smooth interaction with video transcriptions directly.

📁 Comprehensive Document Retrieval: Toggle between full document retrieval and traditional snippets, enabling comprehensive tasks like summarization and supporting enhanced document capabilities.

🌟 RAG Citation Relevance: Easily assess citation accuracy with the addition of relevance percentages in RAG results.

🗂️ Advanced RAG: Improve RAG accuracy with smart pre-processing of chat history to determine the best queries before retrieval.

📚 Inline Citations for RAG: Benefit from seamless inline citations for Retrieval-Augmented Generation (RAG) responses, improving traceability and providing source clarity for newly uploaded files.

📁 Large Text Handling: Optionally convert large pasted text into a file upload to be used directly with RAG, keeping the chat interface cleaner.

🔄 Multi-Modal Support: Effortlessly engage with models that support multi-modal interactions, including images (e.g., LLaVA).

🤖 Multiple Model Support: Quickly switch between different models for diverse chat interactions.

🔀 Merge Responses in Many Model Chat: Enhances the dialogue by merging responses from multiple models into a single, coherent reply.

✅ Multiple Instances of Same Model in Chats: Enhanced many model chat to support adding multiple instances of the same model.

💬 Temporary Chat Feature: Introduced a temporary chat feature, deprecating the old chat history setting to enhance user interaction flexibility.

🖋️ User Message Editing: Enhanced the user chat editing feature to allow saving changes without sending.

💬 Efficient Conversation Editing: Create new message pairs quickly and intuitively using the Cmd/Ctrl+Shift+Enter shortcut, streamlining conversation length tests.

🖼️ Client-Side Image Compression: Save bandwidth and improve performance with client-side image compression, allowing you to compress images before upload from Settings > Interface.

👥 '@' Model Integration: By seamlessly switching to any accessible local or external model during conversations, users can harness the collective intelligence of multiple models in a single chat. This can done by using the @ command to specify the model by name within a chat.

🏷️ Conversation Tagging : Effortlessly categorize and locate tagged chats for quick reference and streamlined data collection using our efficient 'tag:' query system, allowing you to manage, search, and organize your conversations without cluttering the interface.

🧠 Auto-Tagging: Conversations can optionally be automatically tagged for improved organization, mirroring the efficiency of auto-generated titles.

👶 Chat Cloning: Easily clone and save a snapshot of any chat for future reference or continuation. This feature makes it easy to pick up where you left off or share your session with others. To create a copy of your chat, simply click on the Clone button in the chat's dropdown options. Can you keep up with your clones?

⭐ Visualized Conversation Flows: Interactive messages diagram for improved visualization of conversation flows, enhancing understanding and navigation of complex discussions.

📁 Chat Folders: Organize your chats into folders, drag and drop them for easy management, and export them seamlessly for sharing or analysis.

📤 Easy Chat Import: Import chats into your workspace by simply dragging and dropping chat exports (JSON) onto the sidebar.

📜 Prompt Preset Support: Instantly access custom preset prompts using the / command in the chat input. Load predefined conversation starters effortlessly and expedite your interactions. Import prompts with ease through Open WebUI Community integration or create your own!

📅 Prompt Variables Support: Prompt variables such as {{CLIPBOARD}}, {{CURRENT_DATE}}, {{CURRENT_DATETIME}}, {{CURRENT_TIME}}, {{CURRENT_TIMEZONE}}, {{CURRENT_WEEKDAY}}, {{USER_NAME}}, {{USER_LANGUAGE}}, and {{USER_LOCATION}} can be utilized in the system prompt or by using a slash command to select a prompt directly within a chat.

Please note that the {{USER_LOCATION}} prompt variable requires a secure connection over HTTPS. To utilize this particular prompt variable, please ensure that {{USER_LOCATION}} is toggled on from the Settings > Interface menu.
Please note that the {{CLIPBOARD}} prompt variables requires access to your device's clipboard.
🧠 Memory Feature: Manually add information you want your LLMs to remember via the Settings > Personalization > Memory menu. Memories can be added, edited, and deleted.

💻 Model Management
🛠️ Model Builder: All models can be built and edited with a persistent model builder mode within the models edit page.

📚 Knowledge Support for Models: The ability to attach tools, functions, and knowledge collections directly to models from a model's edit page, enhancing the information available to each model.

🗂️ Model Presets: Create and manage model presets for both the Ollama and OpenAI API.

🏷️ Model Tagging: The models workspace enables users to organize their models using tagging.

📋 Model Selector Dropdown Ordering: Models can be effortlessly organized by dragging and dropping them into desired positions within the model workspace, which will then reflect the changes in the model dropdown menu.

🔍 Model Selector Dropdown: Easily find and select your models with fuzzy search and detailed model information with model tags and model descriptions.

⌨️ Arrow Keys Model Selection: Use arrow keys for quicker model selection, enhancing accessibility.

🔧 Quick Actions in Model Workspace: Enhanced Shift key quick actions for hiding/displaying and deleting models in the model workspace.

😄 Transparent Model Usage: Stay informed about the system's state during queries with knowledge-augmented models, thanks to visible status displays.

⚙️ Fine-Tuned Control with Advanced Parameters: Gain a deeper level of control by adjusting model parameters such as seed, temperature, frequency penalty, context length, seed, and more.

🔄 Seamless Integration: Copy any ollama run {model:tag} CLI command directly from a model's page on Ollama library and paste it into the model dropdown to easily select and pull models.

🗂️ Create Ollama Modelfile: To create a model file for Ollama, navigate to the Admin Panel > Settings > Models > Create a model menu.

⬆️ GGUF File Model Creation: Effortlessly create Ollama models by uploading GGUF files directly from Open WebUI from the Admin Settings > Settings > Model > Experimental menu. The process has been streamlined with the option to upload from your machine or download GGUF files from Hugging Face.

⚙️ Default Model Setting: The default model preference for new chats can be set in the Settings > Interface menu on mobile devices, or can more easily be set in a new chat under the model selector dropdown on desktop PCs and laptops.

💡 LLM Response Insights: Details of every generated response can be viewed, including external model API insights and comprehensive local model info.

🕒 Model Details at a Glance: View critical model details, including model hash and last modified timestamp, directly in the Models workspace for enhanced tracking and management.

📥🗑️ Download/Delete Models: Models can be downloaded or deleted directly from Open WebUI with ease.

🔄 Update All Ollama Models: A convenient button allows users to update all their locally installed models in one operation, streamlining model management.

🍻 TavernAI Character Card Integration: Experience enhanced visual storytelling with TavernAI Character Card Integration in our model builder. Users can seamlessly incorporate TavernAI character card PNGs directly into their model files, creating a more immersive and engaging user experience.

🎲 Model Playground (Beta): Try out models with the model playground area (beta), which enables users to test and explore model capabilities and parameters with ease in a sandbox environment before deployment in a live chat environment.

👥 Collaboration
🗨️ Local Chat Sharing: Generate and share chat links between users in an efficient and seamless manner, thereby enhancing collaboration and communication.

👍👎 RLHF Annotation: Enhance the impact of your messages by rating them with either a thumbs up or thumbs down AMD provide a rating for the response on a scale of 1-10, followed by the option to provide textual feedback, facilitating the creation of datasets for Reinforcement Learning from Human Feedback (RLHF). Utilize your messages to train or fine-tune models, all while ensuring the confidentiality of locally saved data.

🔧 Comprehensive Feedback Export: Export feedback history data to JSON for seamless integration with RLHF processing and further analysis, providing valuable insights for improvement.

🤝 Community Sharing: Share your chat sessions with the Open WebUI Community by clicking the Share to Open WebUI Community button. This feature allows you to engage with other users and collaborate on the platform.

To utilize this feature, please sign-in to your Open WebUI Community account. Sharing your chats fosters a vibrant community, encourages knowledge sharing, and facilitates joint problem-solving. Please note that community sharing of chat sessions is an optional feature. Only Admins can toggle this feature on or off in the Admin Settings > Settings > General menu.
🏆 Community Leaderboard: Compete and track your performance in real-time with our leaderboard system, which utilizes the ELO rating system and allows for optional sharing of feedback history.

⚔️ Model Evaluation Arena: Conduct blind A/B testing of models directly from the Admin Settings for a true side-by-side comparison, making it easier to find the best model for your needs.

🎯 Topic-Based Rankings: Discover more accurate rankings with our experimental topic-based re-ranking system, which adjusts leaderboard standings based on tag similarity in feedback.

📂 Unified and Collaborative Workspace : Access and manage all your model files, prompts, documents, tools, and functions in one convenient location, while also enabling multiple users to collaborate and contribute to models, knowledge, prompts, or tools, streamlining your workflow and enhancing teamwork.

📚 History & Archive
📜 Chat History: Access and manage your conversation history with ease via the chat navigation sidebar. Toggle off chat history in the Settings > Chats menu to prevent chat history from being created with new interactions.

🔄 Regeneration History Access: Easily revisit and explore your entire LLM response regeneration history.

📬 Archive Chats: Effortlessly store away completed conversations you've had with models for future reference or interaction, maintaining a tidy and clutter-free chat interface.

🗃️ Archive All Chats: This feature allows you to quickly archive all of your chats at once.

📦 Export All Archived Chats as JSON: This feature enables users to easily export all their archived chats in a single JSON file, which can be used for backup or transfer purposes.

📄 Download Chats as JSON/PDF/TXT: Easily download your chats individually in your preferred format of .json, .pdf, or .txt format.

📤📥 Import/Export Chat History: Seamlessly move your chat data in and out of the platform via Import Chats and Export Chats options.

🗑️ Delete All Chats: This option allows you to permanently delete all of your chats, ensuring a fresh start.

🎙️ Audio, Voice, & Accessibility
🗣️ Voice Input Support with Multiple Providers: Engage with your model through voice interactions using multiple Speech-to-Text providers: Local Whisper (default, with VAD filtering), OpenAI-compatible endpoints, Deepgram, and Azure Speech Services. Enjoy the convenience of talking to your model directly with automatic voice input after 3 seconds of silence for a streamlined experience.

Microphone access requires manually setting up a secure connection over HTTPS to work, or manually whitelisting your URL at your own risk.
😊 Emoji Call: Toggle this feature on from the Settings > Interface menu, allowing LLMs to express emotions using emojis during voice calls for a more dynamic interaction.

Microphone access requires manually setting up a secure connection over HTTPS to work, or manually whitelisting your URL at your own risk.
🎙️ Hands-Free Voice Call Feature: Initiate voice calls without needing to use your hands, making interactions more seamless.

Microphone access requires manually setting up a secure connection over HTTPS to work, or manually whitelisting your URL at your own risk.
📹 Video Call Feature: Enable video calls with supported vision models like LlaVA and GPT-4o, adding a visual dimension to your communications.

Both Camera & Microphone access is required using a secure connection over HTTPS for this feature to work, or manually whitelisting your URL at your own risk.
👆 Tap to Interrupt: Stop the AI’s speech during voice conversations with a simple tap on mobile devices, ensuring seamless control over the interaction.

🎙️ Voice Interrupt: Stop the AI’s speech during voice conversations with your voice on mobile devices, ensuring seamless control over the interaction.

🔊 Multiple Text-to-Speech Providers: Customize your Text-to-Speech experience with multiple providers: OpenAI-compatible endpoints, Azure Speech Services, ElevenLabs (with EU residency support), local Transformers models, and browser-based WebAPI for reading aloud LLM responses.

🔗 Direct Call Mode Access: Activate call mode directly from a URL, providing a convenient shortcut for mobile device users.

✨ Customizable Text-to-Speech: Control how message content is segmented for Text-to-Speech (TTS) generation requests, allowing for flexible speech output options.

🔊 Azure Speech Services Integration: Supports Azure Speech services for Text-to-Speech (TTS), providing users with a wider range of speech synthesis options.

🎚️ Customizable Audio Playback: Allows users to adjust audio playback speed to their preferences in Call mode settings, enhancing accessibility and usability.

🎵 Broad Audio Compatibility: Enjoy support for a wide range of audio file format transcriptions with RAG, including 'audio/x-m4a', to broaden compatibility with audio content within the platform.

🎤 Deepgram Speech-to-Text Integration: Leverage Deepgram's advanced speech recognition capabilities for high-accuracy voice transcription, providing an additional STT option beyond local Whisper and OpenAI.

🔊 ElevenLabs Text-to-Speech Integration: Access ElevenLabs' premium voice synthesis with support for EU residency API endpoints, offering high-quality and natural-sounding voice output for enhanced user experiences.

🔊 Audio Compression: Experimental audio compression allows navigating around the 25MB limit for OpenAI's speech-to-text processing, expanding the possibilities for audio-based interactions.

🗣️ Experimental SpeechT5 TTS: Enjoy local SpeechT5 support for improved text-to-speech capabilities.

🐍 Code Execution
🚀 Versatile, UI-Agnostic, OpenAI-Compatible Plugin Framework: Seamlessly integrate and customize Open WebUI Pipelines for efficient data processing and model training, ensuring ultimate flexibility and scalability.

🛠️ Native Python Function Calling: Access the power of Python directly within Open WebUI with native function calling. Easily integrate custom code to build unique features like custom RAG pipelines, web search tools, and even agent-like actions via a built-in code editor to seamlessly develop and integrate function code within the Tools and Functions workspace.

🐍 Python Code Execution: Execute Python code locally in the browser via Pyodide with a range of libraries supported by Pyodide.

🌊 Mermaid Rendering: Create visually appealing diagrams and flowcharts directly within Open WebUI using the Mermaid Diagramming and charting tool, which supports Mermaid syntax rendering.

🔗 Iframe Support: Enables rendering HTML directly into your chat interface using functions and tools.

🔒 Integration & Security
✨ Multiple OpenAI-Compatible API Support: Seamlessly integrate and customize various OpenAI-compatible APIs, enhancing the versatility of your chat interactions.

🔑 Simplified API Key Management: Easily generate and manage secret keys to leverage Open WebUI with OpenAI libraries, streamlining integration and development.

🌐 HTTP/S Proxy Support: Configure network settings easily using the http_proxy or https_proxy environment variable. These variables, if set, should contain the URLs for HTTP and HTTPS proxies, respectively.

🌐🔗 External Ollama Server Connectivity: Seamlessly link to an external Ollama server hosted on a different address by configuring the environment variable.

🛢️ Flexible Database Integration: Seamlessly connect to custom databases, including SQLite, Postgres, and multiple vector databases like Milvus, using environment variables for flexible and scalable data management.

🗄️ Multiple Vector Database Support: Choose from 9 vector database options for optimal RAG performance: ChromaDB (default), PostgreSQL with PGVector, Qdrant, Milvus, Elasticsearch, OpenSearch, Pinecone, S3Vector, and Oracle 23ai. Each option provides different scaling characteristics and performance profiles to match your deployment needs.

☁️ Enterprise Cloud Storage Backends: Configure cloud storage backends including Amazon S3 (with S3-compatible providers like MinIO), Google Cloud Storage, and Microsoft Azure Blob Storage for scalable file storage, enabling stateless instances and distributed deployments.

📂 Cloud File Picker Integration: Import documents directly from Google Drive and OneDrive/SharePoint through native file picker interfaces, streamlining workflows for users working with enterprise cloud storage solutions.

🌐🗣️ External Speech-to-Text Support: The addition of external speech-to-text (STT) services provides enhanced flexibility, allowing users to choose their preferred provider for seamless interaction.

🌐 Remote ChromaDB Support: Extend the capabilities of your database by connecting to remote ChromaDB servers.

🔀 Multiple Ollama Instance Load Balancing: Effortlessly distribute chat requests across multiple Ollama instances for enhanced performance and reliability.

🚀 Advanced Load Balancing and Reliability: Utilize enhanced load balancing capabilities, stateless instances with full Redis support, and automatic web socket re-connection to promote better performance, reliability, and scalability in WebUI, ensuring seamless and uninterrupted interactions across multiple instances.

☁️ Cloud Storage Backend Support: Enable stateless Open WebUI instances with cloud storage backends (Amazon S3, Google Cloud Storage, Microsoft Azure Blob Storage) for enhanced scalability, high availability, and balancing heavy workloads across multiple instances.

🛠️ OAuth Management for User Groups: Enhance control and scalability in collaborative environments with group-level management via OAuth integration.

🔐 SCIM 2.0 Automated Provisioning: Enterprise-grade user and group provisioning through SCIM 2.0 protocol, enabling seamless integration with identity providers like Okta, Azure AD, and Google Workspace for automated user lifecycle management, reducing administrative overhead.

📊 OpenTelemetry Observability: Export traces, metrics, and logs to your observability stack using OpenTelemetry protocol (OTLP), supporting both gRPC and HTTP exporters with configurable endpoints, authentication, and sampling strategies for comprehensive production monitoring.

👑 Administration
👑 Super Admin Assignment: Automatically assigns the first sign-up as a super admin with an unchangeable role that cannot be modified by anyone else, not even other admins.

🛡️ Granular User Permissions: Restrict user actions and access with customizable role-based permissions, ensuring that only authorized individuals can perform specific tasks.

👥 Multi-User Management: Intuitive admin panel with pagination allows you to seamlessly manage multiple users, streamlining user administration and simplifying user life-cycle management.

🔧 Admin Panel: The user management system is designed to streamline the on-boarding and management of users, offering the option to add users directly or in bulk via CSV import.

👥 Active Users Indicator: Monitor the number of active users and which models are being utilized by whom to assist in gauging when performance may be impacted due to a high number of users.

🔒 Default Sign-Up Role: Specify the default role for new sign-ups to pending, user, or admin, providing flexibility in managing user permissions and access levels for new users.

🔒 Prevent New Sign-Ups: Enable the option to disable new user sign-ups, restricting access to the platform and maintaining a fixed number of users.

🔒 Prevent Chat Deletion: Ability for admins to toggle a setting that prevents all users from deleting their chat messages, ensuring that all chat messages are retained for audit or compliance purposes.

🔗 Webhook Integration: Subscribe to new user sign-up events via webhook (compatible with Discord, Google Chat, Slack and Microsoft Teams), providing real-time notifications and automation capabilities.

📣 Configurable Notification Banners: Admins can create customizable banners with persistence in config.json, featuring options for content, background color (info, warning, error, or success), and dismissibility. Banners are accessible only to logged-in users, ensuring the confidentiality of sensitive information.

🛡️ Model Whitelisting: Enhance security and access control by allowing admins to whitelist models for users with the user role, ensuring that only authorized models can be accessed.

🔑 Admin Control for Community Sharing: Admins can enable or disable community sharing for all users via a toggle in the Admin Panel > Settings menu. This toggle allows admins to manage accessibility and privacy, ensuring a secure environment. Admins have the option of enabling or disabling the Share on Community button for all users, which allows them to control community engagement and collaboration.

📧 Trusted Email Authentication: Optionally authenticate using a trusted email header, adding an extra layer of security and authentication to protect your Open WebUI instance.

🔒 Backend Reverse Proxy Support: Bolster security through direct communication between Open WebUI's backend and Ollama. This key feature eliminates the need to expose Ollama over the local area network (LAN). Requests made to the /ollama/api route from Open WebUI are seamlessly redirected to Ollama from the backend, enhancing overall system security and providing an additional layer of protection.

🔒 Authentication: Please note that Open WebUI does not natively support federated authentication schemes such as SSO, OAuth, SAML, or OIDC. However, it can be configured to delegate authentication to an authenticating reverse proxy, effectively achieving a Single Sign-On (SSO) experience. This setup allows you to centralize user authentication and management, enhancing security and user convenience. By integrating Open WebUI with an authenticating reverse proxy, you can leverage existing authentication systems and streamline user access to Open WebUI. For more information on configuring this feature, please refer to the Federated Authentication Support.

🔓 Optional Authentication: Enjoy the flexibility of disabling authentication by setting WEBUI_AUTH to False. This is an ideal solution for fresh installations without existing users or can be useful for demonstration purposes.

🚫 Advanced API Security: Block API users based on customized model filters, enhancing security and control over API access.

❗ Administrator Updates: Ensure administrators stay informed with immediate update notifications upon login, keeping them up-to-date on the latest changes and system statuses.

👥 User Group Management: Create and manage user groups for seamless organization and control.

🔐 Group-Based Access Control: Set granular access to models, knowledge, prompts, and tools based on user groups, allowing for more controlled and secure environments.

🛠️ Granular User Permissions: Easily manage workspace permissions, including file uploads, deletions, edits, and temporary chats, as well as model, knowledge, prompt, and tool creation.

🔑 LDAP Authentication: Enhance security and scalability with LDAP support for user management.

🔐 SCIM 2.0 Provisioning: Automate user and group lifecycle management through SCIM 2.0 protocol integration with identity providers like Okta, Azure AD, and Google Workspace, reducing administrative overhead and ensuring synchronized user management across systems.

🌐 Customizable OpenAI Connections: Enjoy smooth operation with custom OpenAI setups, including prefix ID support and explicit model ID support for APIs.

🔐 Ollama API Key Management: Manage Ollama credentials, including prefix ID support, for secure and efficient operation.

🔄 Connection Management: Easily enable or disable individual OpenAI and Ollama connections as needed.

🎨 Intuitive Model Workspace: Manage models across users and groups with a redesigned and user-friendly interface.

🔑 API Key Authentication: Tighten security by easily enabling or disabling API key authentication.

🔄 Unified Model Reset: Reset and remove all models from the Admin Settings with a one-click option.

🔓 Flexible Model Access Control: Easily bypass model access controls for user roles when not required, using the 'BYPASS_MODEL_ACCESS_CONTROL' environment variable, simplifying workflows in trusted environments.

🔒 Configurable API Key Authentication Restrictions: Flexibly configure endpoint restrictions for API key authentication, now off by default for a smoother setup in trusted environments.

Edit this page
Previous
API Endpoints
Next
Federated Authentication
Key Features of Open WebUI ⭐
And many more remarkable features including... ⚡️
🔧 Pipelines Support
🖥️ User Experience
💬 Conversations
💻 Model Management
👥 Collaboration
📚 History & Archive
🎙️ Audio, Voice, & Accessibility
🐍 Code Execution
🔒 Integration & Security
👑 Administration
Docs
Getting Started
FAQ
Help Improve The Docs
Community
GitHub
Discord
Reddit
𝕏
More
Release Notes
About
Report a Vulnerability / Responsible Disclosure




 🚅 LiteLLM
Hiring

Features

Pricing

Enterprise

Changelog

Docs

Github 30K

Compare features
Free
Get Started

Enterprise
Get Started

Pass-through Endpoints
Useful for migrating existing projects to the proxy. The request is passed to the provider's endpoint and the response is then passed back to the client. No translation is done.

Cost Tracking

Logging

End-user Tracking

Using LiteLLM Virtual Keys/Authentication

Logging
LLM Observability Tools (Langfuse, Langsmith, etc.)

Datadog Logging

S3 Logging

GCS Logging

Azure Data Lake

Key/Team-based Logging

Alerting/Monitoring
Slack/Discord/Teams/Email/ Webhook

Pagerduty Alerting

Prometheus Metrics

Authentication
Virtual Keys

Custom Auth

OIDC/JWT Auth

Virtual Key Rotation

Write Key to Secret Manager

CRUD Endpoints + UI
Create / Manage Users

Create / Manage Teams

Create / Manage Orgs

Assign Team Admins

Assign Org Admins

Control Model Access
Restrict Models by Key/User/Team

Model Access Groups

Team-only Models

Admin UI
Internal User Self-serve

SSO

Auto-add SSO User to Teams

Spend Tracking
Track Spend by Model/Key/User/Team

Track Spend for Org

Track Spend for Custom Tags

API endpoints for Spend Reporting

Budgets + Rate Limits
Set Budgets by Key/User/Team

Set Rate Limits by Key/User/Team

Temporary Budget Increase

Budget/Rate Limit Tiers

Guardrails
Set Guardrails per request

Default-on Guardrails

Set Guardrails by Key/Team

 🚅 LiteLLM


Product

LiteLLM Python SDK

LiteLLM Gateway (Proxy)

Docs

Getting Started - LiteLLM Gateway

Supported LLM Providers

Logging - Langfuse, OpenTelemetry etc

Prometheus Metrics

Virtual Keys

Company

Schedule call with Founders

Legal/Security/Compliance FAQ

Why Enterprise?

Careers

Resources

Slack/Discord

Docs

Get latest updates here




All Features of AnythingLLM
Click the below cards to know more about the features

AI Agents
→
API Access & Keys
→
Appearance Customization
→
Chat Logs
→
Chat Modes
→
Embedded Chat Widgets
→
Event Logs
→
Large Language Models
→
Embedding Models
→
Transcription Models
→
Vector Databases
→
Security & Access
→
Privacy & Data Handling
→
Cloud Deployment
→
System Prompt Variables
→
Last updated on September 18, 2025
Introduction




🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

Edit this page
Scroll to top
Feature Overview
AI Agents
AnythingLLM AI Agents
AI Agents
Agents are basically an LLM that has access to some simple tools. We will be adding much more customization in this area soon. All agents share the same tools across workspaces, but operate within the workspace they were invoked via @agent.

You can start an agent session by going into any workspace and typing @agent <your prompt> and exit by just typing exit

Agents can scrape websites, list and summarize your documents, search the web, make charts, and even save files to desktop and their own memory.

Examples:
1: @agent what documents can you see - > LLM will "look" at what are the documents it can see

2: @agent summarize readme.pdf - > LLM will summarize that specific embedded file

AnythingLLM AI Agents
View all the available @agent skills →
Last updated on September 18, 2025
All Features
Private Browser Tool
MIT 2025 © Mintplex Labs.
AI Agents ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Key Features
Using the Authenticated Scraping Tool
Accessing the Tool
Authentication Process
Managing Browser Data
Common Use Cases
Troubleshooting
Edit this page
Scroll to top
Feature Overview
Private Browser Tool
Desktop Only Feature (v1.8.3+)
The Authenticated Scraping tool is exclusively available in the AnythingLLM Desktop application!

Authenticated Scraping
Security Note All credentials and session data are stored locally on your machine. AnythingLLM never transmits or stores your login information outside of your local machine.

The Authenticated Scraping tool enables you to access and scrape gated online content from websites or services that require authentication but hold critical contexual content you might want to use in your workflows, such as your personal LinkedIn feed or internal company portals that you have access to.

Your LLM can now access these websites and scrape and view content just like you would in a regular browser!


Key Features
Secure Session Storage: Credentials are stored locally using isolated browser sessions
Session Persistence: Login sessions persist between app restarts until explicitly cleared or the authentication expires for the associated service
Isolated Environment: Separate from your actual web browser
Full User Control: Clear stored data or sessions at any time with a single click
Using the Authenticated Scraping Tool
Accessing the Tool
Open AnythingLLM Desktop
Navigate to Settings > Tools > Browser Tool
Click "Open Private Browser" to launch the isolated browser window

Authentication Process
Log into your desired service (e.g., LinkedIn, Gmail) through the Authenticated Scraping tool.
Your session will persist until you explicitly clear the browser data or the authentication expires for the associated service.
AnythingLLM can now access authenticated content from these services when scraping or via agentic workflow execution.
The returned content will be text only. No images, videos, or other media will be returned.
Heads up! The Authenticated Scraping tool is not a magic bullet. It is a tool that allows you to access authenticated content from websites that require authentication. It cannot currently interact with the content of the page you are accessing (eg: browser automation, RPA, etc).

Managing Browser Data
Clearing Data: Use the "Clear Browser Data" button to remove all stored credentials and sessions
When should you clear the browser data?:
When switching between different service accounts
If you encounter authentication issues when the LLM tries to access the site you want to scrape
Common Use Cases
Warning! Some web services may detect and restrict automated access, even though this tool functions as a standard browser. Use this feature responsibly and at your own discretion, as certain services may suspend or block accounts that they perceive as engaging in automated activity.

Scraping your personal linkedin profile or feed.
Accessing internal company documentation that is behind a login or SSO portal.
Collecting or accessing data from paid or authenticated web service you have access to normally.
Troubleshooting
If you encounter issues:

Clear the browser data and try again
Ensure you're fully logged into the service by opening the private browser and navigating to the site you want the LLM to access.
Some services have very short lived sessions, those services may require you to log in again after a certain amount of time or might be a bad use-case for this tool. You can always re-authenticate with the service by opening the private browser and navigating to the site you want the LLM to access and logging in again to refresh the session.

Last updated on October 31, 2025
AI Agents
API Access
MIT 2025 © Mintplex Labs.
Authenticated Scraping ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

Edit this page
Scroll to top
Feature Overview
API Access
AnythingLLM
API Access & Keys
You can find the API documentation for available endpoints on your instance at /api/docs

API keys are managed by accounts with the correct access level.

However, anyone with the API key can use the AnythingLLM API, so do not share or publish this key anywhere.

AnythingLLM supports a full developer API that you can use to manage, update, embed, and even chat with your workspaces.

You can create and delete API keys on the fly if you are allowed permission to do so.

AnythingLLM
Last updated on September 18, 2025
Private Browser Tool
Appearance Customization
MIT 2025 © Mintplex Labs.
API Access & Keys ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Custom Logo
Custom Welcome Messages
Custom Footer Links and Icons
Edit this page
Scroll to top
Feature Overview
Appearance Customization
AnythingLLM Appearance Customization
Appearance Customization
DOCKER VERSION ONLY!

These settings are only available in the Docker version of AnythingLLM

AnythingLLM allows you to customize the look and feel of your instance to match your brand and identity.

Appearance Settings Page
Overview of all the appearance settings available in AnythingLLM.

Custom Logo
Custom Logo
You can replace the AnythingLLM branded logo that appears on the login page and throughout the app with your own brand's logo. In this example, we have used a green square image for demonstration purposes.

Custom Welcome Messages
Custom Welcome Messages
By default, when you first log in to AnythingLLM and you have not yet selected a workspace, you will be shown the default messages explaining AnythingLLM. Using the system messages inputs, you can simulate both system and user response messages. Take this opportunity to tell users what specific workspaces are for - or just say hello!

Custom Footer Links and Icons
Custom Footer Links and Icons
The footer icons can be replaced with custom links and icons to provide quick access to relevant resources or web pages.

Last updated on September 18, 2025
API Access
Chat Logs
MIT 2025 © Mintplex Labs.
Appearance Customization ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

Edit this page
Scroll to top
Feature Overview
Chat Logs
AnythingLLM Workspace Chat Logs
Workspace Chat Logs
AnythingLLM supports exporting chats as:

CSV
JSON
JSON (Alpaca)
JSONL (OpenAI fine-tune)
Just click export at the top of the screen once at least 10 chat logs are available! Provided you have the correct account permissions, you can view the chat logs per workspace and per user of your AnythingLLM instance.

AnythingLLM Workspace Chat Logs
Last updated on September 18, 2025
Appearance Customization
Chat Modes
MIT 2025 © Mintplex Labs.
Workspace Chat Logs ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Query Mode vs Chat Mode
Common Questions
"It keeps saying 'No relevant information found' in Query mode"
"When should I use Query mode vs Chat mode?"
"Why does it work better with some documents than others?"
Tips for Better Results
Edit this page
Scroll to top
Feature Overview
Chat Modes
Chat Modes in AnythingLLM
AnythingLLM offers two ways to chat with your documents: Query mode and Chat mode. Let's understand what each does and how to get the best results.

Query Mode vs Chat Mode
Query Mode:

Only uses information from your uploaded documents
Will tell you if it can't find relevant information
Best for when you need accurate, document-based answers
Chat Mode:

Uses both your documents and the AI's general knowledge
More conversational and flexible
Good for brainstorming and exploring topics
Common Questions
"It keeps saying 'No relevant information found' in Query mode"
This usually means one of three things:

The information might be in your document but worded differently
The similarity settings might be too strict
The document might be too large and split in a way that makes finding information difficult
Quick fixes to try:

Go to workspace settings → Vector Database Settings
Change "Document similarity threshold" to "No restriction"
Try asking your question using words that match how it's written in your document
Instead of asking "How do I start the app?", try using terms from your document like "How do I initialize the application?"

"When should I use Query mode vs Chat mode?"
Use Query mode when:

You need factual answers from your documents
You're working with technical documentation
You want to prevent made-up information
Use Chat mode when:

You want more conversational responses
You need additional context or examples
You're brainstorming ideas
"Why does it work better with some documents than others?"
Documents are processed in chunks, and each chunk is analyzed separately. This means:

Large documents might need more specific questions
Technical documents work better with technical questions
Tips for Better Results
Start with Query mode and "No restriction" similarity if you're not finding information
Use specific terms from your documents in your questions
Switch to Chat mode if you need more context or explanation
Try rephrasing your question if you're not getting good results
If you're still not getting good results, check your workspace settings and try adjusting the "Document similarity threshold" between No restriction, Low (≥ .25), Medium (≥ .50), or High (≥ .75) to find what works best for your documents.

Last updated on September 18, 2025
Chat Logs
Embedded Chat Widgets
MIT 2025 © Mintplex Labs.
Chat Modes ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Configuration Options
Workspace
Allowed Chat Method
Restrict Requests from Domains
Max Chats per Day
Max Chats per Session
Enable Dynamic Model Use
Enable Dynamic LLM Temperature
Enable Prompt Override
Embedding the Chat Widget
Edit this page
Scroll to top
Feature Overview
Embedded Chat Widgets
AnythingLLM Embedded Chat Widgets
Embedded Chat Widgets
DOCKER VERSION ONLY!

These settings are only available in the Docker version of AnythingLLM

Embedded Chat Widget
AnythingLLM allows you to create embedded chat widgets that can be easily integrated into any website using a simple <script> tag. These embedded chat widgets provide a convenient way for users to interact with your chatbot directly from your website.

Configuration Options
When creating an embedded chat widget, you have several configuration options available to customize its behavior and appearance.

Embedded Chat Options 1
Workspace
The workspace setting determines which workspace your chat window will be based on. All defaults will be inherited from the selected workspace unless overridden by the specific configuration options.

Allowed Chat Method
You can set how your chatbot should operate using the allowed chat method. There are two options:

Chat: The chatbot will respond to all questions regardless of context.
Query: The chatbot will only respond to chats related to documents in the workspace.
Restrict Requests from Domains
This filter allows you to block any requests that come from domains other than the specified list. Leaving this field empty means anyone can use your embedded chat widget on any site.

Embedded Chat Options 2
Max Chats per Day
You can limit the number of chats this embedded chat widget can process in a 24-hour period. Setting this value to zero means unlimited chats per day.

Max Chats per Session
You can limit the number of chats a session user can send with this embedded chat widget in a 24-hour period. Setting this value to zero means unlimited chats per session.

Enable Dynamic Model Use
By enabling dynamic model use, you allow the setting of the preferred LLM model to override the workspace default.

Enable Dynamic LLM Temperature
Enabling dynamic LLM temperature allows the setting of the LLM temperature to override the workspace default.

Enable Prompt Override
By enabling prompt override, you allow the setting of the system prompt to override the workspace default.

Embedding the Chat Widget
Embedded Chat Code
After creating an embedded chat widget, you will be provided with a link that you can publish on your website using a simple <script> tag. This allows you to easily integrate the chat widget into your website's HTML code.

Last updated on September 18, 2025
Chat Modes
Event Logs
MIT 2025 © Mintplex Labs.
Embedded Chat Widgets ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Event Types
Event Details
Edit this page
Scroll to top
Feature Overview
Event Logs
AnythingLLM Event Logs
Event Logs
The Event Logs page in AnythingLLM allows users to view and monitor various events that occur within the application.

AnythingLLM Event Logs
This feature provides insights into user activities and system-related events.

Event Types
The Event Logs page captures a variety of events, such as:

User login attempts (successful and failed)
Messages sent by users
Changes made to application settings
Document uploads
Event Details
Each event in the Event Logs page includes relevant information, such as the event type, associated user (if applicable), timestamp, and any additional details specific to the event type.

Useful for monitoring your AnythingLLM instance.

Last updated on September 18, 2025
Embedded Chat Widgets
Embedding Models
MIT 2025 © Mintplex Labs.
Event Logs ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Supported Embedding Model Providers
Local Embedding Model Providers
Cloud Embedding Model Providers
Edit this page
Scroll to top
Feature Overview
Embedding Models
AnythingLLM Embedding Models
Embedding Models
AnythingLLM supports many embedding model providers out of the box with very little, if any setup.

Embedding models are specific types of models that turn text into vectors, which can be stored and searched in a vector database - which is the foundation of RAG.

Supported Embedding Model Providers
Local Embedding Model Providers
Built-in (default)
→
Ollama
→
LM Studio
→
Local AI
→
Cloud Embedding Model Providers
OpenAI
→
Azure OpenAI
→
Cohere
→
Last updated on September 18, 2025
Event Logs
Language Models
MIT 2025 © Mintplex Labs.
Embedding Models ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Supported Language Model Providers
Local Language Model Providers
Cloud Language Model Providers
Edit this page
Scroll to top
Feature Overview
Language Models
AnythingLLM Large Language Models
Large Language Models
Tip: Models that are multi-modal (text-to-text & image-to-text) are supported for System & Workspace models.

AnythingLLM allows you to use a host of LLM providers for chatting and generative AI.

Depending on your selection additional configuration might be required.

Supported Language Model Providers
Local Language Model Providers
Built-in (default)
→
Ollama
→
LM Studio
→
Local AI
→
Cloud Language Model Providers
OpenAI
→
Azure OpenAI
→
AWS Bedrock
→
Anthropic
→
Cohere
→
Google Gemini Pro
→
Hugging Face
→
Together AI
→
OpenRouter
→
Perplexity AI
→
Mistral API
→
Groq
→
KobaldCPP
→
OpenAI (generic)
→
Last updated on September 18, 2025
Embedding Models
Transcription Models
MIT 2025 © Mintplex Labs.
Large Language Models ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Supported Transcription Model Providers
Local Transcription Model Providers
Cloud Transcription Model Providers
Edit this page
Scroll to top
Feature Overview
Transcription Models
AnythingLLM Transcription Models
Transcription Models
AnythingLLM supports custom audio transcription providers.

Supported Transcription Model Providers
Local Transcription Model Providers
Built-in (Xenova)
→
Cloud Transcription Model Providers
OpenAI
→
Last updated on September 18, 2025
Language Models
Vector Database
MIT 2025 © Mintplex Labs.
Transcription Models ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Supported Vector Databases
Local Vector Databases Providers
Cloud Vector Databases Providers
Edit this page
Scroll to top
Feature Overview
Vector Database
AnythingLLM Vector Databases
Vector Databases
AnythingLLM comes with a private built-in vector database powered by LanceDB. Your vectors never leave AnythingLLM when using the default option.

AnythingLLM supports many vector databases providers out of the box.

Supported Vector Databases
Local Vector Databases Providers
LanceDB (Built-in)
→
PGVector
→
Chroma
→
Milvus
→
Cloud Vector Databases Providers
Pinecone
→
Zilliz
→
AstraDB
→
QDrant
→
Weaviate
→
Last updated on September 18, 2025
Transcription Models
Security & Access
MIT 2025 © Mintplex Labs.
Vector Databases ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Single-user Mode
Password Protecting the Instance
Multi-user Mode
User Roles
Enabling Multi-user Mode
Edit this page
Scroll to top
Feature Overview
Security & Access
AnythingLLM Security and Access
Security and Access
DOCKER VERSION ONLY!

These settings are only available in the Docker version of AnythingLLM

AnythingLLM supports two types of use cases: single-user and multi-user mode.

Single-user Mode
Single-user mode is preferred for those who only themselves or a select group of trusted people will use the instance. If you want to have per-user permissions, you should switch to multi-user mode.

In single-user mode, you (and only you) have complete control over the instance. Anyone with the password to the instance, if set, will be able to use the instance, change any configuration or settings, and view all chats.

Password Protecting the Instance
When using AnythingLLM in "single user mode," you can password protect the instance by toggling on the "Password Protect Instance" option. This will display an input where you can enter the password to protect the instance.

Password Protect Instance
You can turn off password protection at any time or reset the password to the instance while logged in.

Multi-user Mode
Warning

Once in multi-user mode, you cannot revert back to single-user mode

The preferred method of use for AnythingLLM is multi-user mode. In this mode, you can set per-user role-based access permissions.

By default, you will create the administrator account, which has the highest level of privilege. As an administrator, you will have access to the entire system, logs, analytics, and more.

User Roles
Admin: Full access to the entire system
Manager: Can view all workspaces and manage all properties except for settings for LLM, Embedder, and Vector database
Default: Can only send chats to workspaces they are explicitly added to. Cannot see or edit any workspaces or system settings.
Enabling Multi-user Mode
To enable multi-user mode, toggle on the "Enable multi-user mode" option. This will display an input where you can enter the username and password for the first admin account.

Enable Multi-user Mode
This will be the default admin account that you will use to control the instance. Once set, you will be logged out so you can log in with the new password.

Last updated on September 18, 2025
Vector Database
Privacy & Data Handling
MIT 2025 © Mintplex Labs.
Security and Access ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Anonymous Telemetry
Edit this page
Scroll to top
Feature Overview
Privacy & Data Handling
AnythingLLM Privacy & Data
Privacy & Data Handling
Tip:

AnythingLLM is transparent telling you who and what has access to your data.

Privacy & Data
Anonymous Telemetry
AnythingLLM collects anonymous telemetry and never collects any of your personal data.

We collect telemetry to help improve our product.

If for any reason you would not like to participate in sharing telemetry with us, you can disable it in this menu.

Last updated on September 18, 2025
Security & Access
System Prompt Variables
MIT 2025 © Mintplex Labs.
Privacy & Data ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Default Variables
Custom Variables
How to use system prompt variables
UI Example:
Edit this page
Scroll to top
Feature Overview
System Prompt Variables
System Prompt Variables
System prompt variables allow you to inject dynamic and static variables into your system prompt on the fly. This is useful for a variety of use cases, such as:

Injecting the user's name into the system prompt
Injecting the current date and time into the system prompt
Injecting static information into the system prompt like your company's name
and more!
Default Variables
AnythingLLM can have varying default variables depending on if you are using the AnythingLLM via Docker or AnythingLLM Desktop version.

AnythingLLM comes with a set of default variables that you can use in your system prompt. You can view the full list of active variables by clicking on the System Prompt Variables link in the sidebar under Tools when on the settings page.

AnythingLLM System Prompt Variables
Variable	Description	Available in
{date}	The current date	ALL VERSIONS
{time}	The current time	ALL VERSIONS
{datetime}	The current date and time	ALL VERSIONS
{user.name}	The name of the user	AnythingLLM Docker (with multi-user mode enabled)
{user.bio}	The bio field of the user	AnythingLLM Docker (with multi-user mode enabled)
{os.name}	The name of the operating system	AnythingLLM Desktop
{os.arch}	The architecture of the operating system	AnythingLLM Desktop
Note: Any time based variable will the current time of the machine AnythingLLM is running on. Keep this in mind in Docker based versions of AnythingLLM.

Custom Variables
You can also create your own custom variables by clicking the Add Variable button on the System Prompt Variables page.

AnythingLLM Custom Variables
All user created variables are static values and will not change when expanded into a system prompt.

How to use system prompt variables
Invalid variables will simply not be expanded into the system prompt - you will not see an error message during an LLM request.

You can tell if a variable is invalid once you stop editing the system prompt and it is not highlighted in blue in the UI.

System prompt variables can be used any workspace's System Prompt field. You can inject a variable by editing the system prompt and using the variable in the prompt.

Example:

You are a helpful assistant.
Today is {date} and the current time is {time}.
The user's name is {user.name}, they work at {company_name} and this is what we know about them:
{user.bio}
When expanded into a system prompt, it will look like this:

You are a helpful assistant.
Today is 2024-01-01 and the current time is 12:00:00.
The user's name is John Doe, they work at Google and this is what we know about them:
Rock climbing is my favorite hobby and I am obsessed with optimizing AI agents and workflows.
UI Example:
AnythingLLM System Prompt Variables
Last updated on September 18, 2025
Privacy & Data Handling
Overview
MIT 2025 © Mintplex Labs.
System Prompt Variables ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

User messages
Actions
LLM messages
Actions
Prompt Input Controls
Edit this page
Scroll to top
Chat Interface overview
AnythingLLM Chat UI
Overview of the chat interface
The chat interface of AnythingLLM is where you will spend most of your time when using AnythingLLM, as such you should familiarize yourself with the basics. This page could have some additional icons that are not in the above image, as we are always improving AnythingLLM.

The above image may seem like a lot, but you will soon find the interface intuitive and familiar with other interfaces you have used.

User messages
User messages are messages that you have sent. This is the text that is used to find similar documents as well as what is sent to the LLM.

Actions
Copy: Copy the content of this text box.
Edit: Editing a message allows you to amend and automatically resubmit the conversation from that point to the LLM. Beware that this will truncate all messages below the edited content.
Speak: Use the operating system native text-to-speech module, OpenAI Voice, or an 11Labs voice to speak your text.
LLM messages
LLM messages are responses from your LLM that are active in this chat session. This is the text that is used to find similar documents as well as what is sent in future conversations. History is automatically managed when the context window is exceeded.

Actions
Copy: Copy the content of this text box.
Edit: Editing a message allows you to amend the output of an LLM message for correctness. This does not resubmit your prompt and simply will update the history.
Regenerate: Resend a prompt back to the LLM with the same prompt and history to get a new answer.
Feedback (Thumbs Up & Thumbs Down): Allow the user to leave qualitative feedback on an LLM response. Leaving feedback has no impact on message history or future responses. Feedback metrics are most useful for exporting of chats to be able to sort through good responses for creating fine-tunes outside of AnythingLLM.
Prompt Input Controls
Slash Commands: Slash Commands are ways to inject some standard text into your prompt where that command is present. It is basically a short-key for text snippets. You can create and manager your slash commands here.
Default Slash Commands: These are special commands built by the core-team that have special functions like /reset
@agent Invocation: View all available @agents and their available skill sets. Using @agent at the start of a prompt will start an agent session. Learn more about agents here.
Font Size: Set the default font size for your profile of AnythingLLM.
Microphone: Enable voice-to-text inputs for your LLM prompts.This feature is not available on Desktop.
Last updated on September 18, 2025
Zilliz
Other configurations
MIT 2025 © Mintplex Labs.
ChatUI Walkthrough ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
What is NVIDIA NIM?
System Requirements
Installation Walkthrough
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Privacy
How does it work?
What models are supported?
How do I install it?
Definitions
Video Walkthrough & Overview
Edit this page
Scroll to top
NVIDIA NIM Integration
What is NVIDIA NIM?
NVIDIA NIM is being phased out of AnythingLLM Desktop and will be removed in a future version.

As an alternative, we recommend using Microsoft Foundry Local which is a free and open source LLM engine that runs on your local machine.

You are also welcome to use any other local LLM engine like Ollama or LM Studio or our internal built in LLM engine that comes with AnythingLLM Desktop.

What is NVIDIA NIM?
NVIDIA NIM (aka: Nvidia Inference Microservices) is a software technology, which packages optimized inference engines, industry-standard APIs and support for AI models into containers for easy deployment.

All of this runs via WSL2 on Windows and makes it easy to deploy and run LLM models locally at the fastest speeds possible on RTX AI PC's. AnythingLLM features a bespoke integration in the AnythingLLM Desktop client that makese installation, setup, and usage of NIM a breeze.

NVIDIA NIM is currently in beta and is only available on Windows 11 on AnythingLLM Desktop.

Privacy
NVIDIA NIM models run fully locally on your machine using your own GPU. AnythingLLM does not send any data to NVIDIA or any other third party in order to run NIM models. After a model is installed, it is present on your local machine and AnythingLLM will use this local engine for inference.

NVIDIA NIM on RTX is not to be confused with NVIDIA's cloud-based NIM offering. This is a completely separate product and service designed to run NIM on your local RTX GPU.

How does it work?
A NIM is a single model + software stack, packaged into a container designed and maintained by NVIDIA. It is specificially designed to be run on NVIDIA RTX GPUs. In AnythingLLM, we use NIM to run the LLM models for chat, agents, and all other tasks that require inference.

See the NVIDIA NIM system requirements for the full list of requirements to run NIM models on your system.

What models are supported?
AnythingLLM supports all of the models that are available in the NIM containers. You can see the full list of models on build.nvidia.com.

How do I install it?
AnythingLLM will present you with a simple to use UI to install and manage NIM containers if you select the NVIDIA NIM LLM provider and are on a compatible operating system.

Once the official NIM installer has finished, you will be able to use NVIDIA NIM models in AnythingLLM.

See the NVIDIA NIM x AnythingLLM Walkthrough for the full walkthrough.

Definitions
NIM: Nvidia Inference Microservice - a single LLM or Model + software stack, packaged into a container designed and maintained by NVIDIA.
WSL2: Windows Subsystem for Linux 2 - a compatibility layer that allows you to run Linux binaries on Windows 11. You will not need to directly interact with WSL2 - the NIM installer will handle this for you and AnythingLLM will use it automatically.
NIM Installer: The pre-built NVIDIA NIM installer that runs in the AnythingLLM Desktop client to unlock the use of NIM models in AnythingLLM.
NIM Manager: The AnythingLLM UI that allows you to install, update, and run a NIM.
Video Walkthrough & Overview

Last updated on October 9, 2025
Install the AnythingLLM Browser Extension
System Requirements
MIT 2025 © Mintplex Labs.
What is NVIDIA NIM? ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
What is NVIDIA NIM?
System Requirements
Installation Walkthrough
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Select the NVIDIA NIM LLM Provider
Fresh install
Post install
Running the NIM Installer
Swap to Managed Mode
Installing your first model
Monitoring your model download
Starting your first NIM
Streaming logs from the NIM
How do I know when my NIM is ready to use?
Selecting your NIM in AnythingLLM
Stopping your NIM
Deleting your NIM
Edit this page
Scroll to top
NVIDIA NIM Integration
Installation Walkthrough
NVIDIA NIM is being phased out of AnythingLLM Desktop and will be removed in a future version.

As an alternative, we recommend using Microsoft Foundry Local which is a free and open source LLM engine that runs on your local machine.

You are also welcome to use any other local LLM engine like Ollama or LM Studio or our internal built in LLM engine that comes with AnythingLLM Desktop.

NVIDIA NIM Walkthrough
The use of NVIDIA NIM in AnythingLLM is very simple and straightforward - all of the complexity is hidden from you by the AnythingLLM Desktop client or the NVIDIA NIM Installer.

Select the NVIDIA NIM LLM Provider
In AnythingLLM Desktop, select the NVIDIA NIM LLM provider from the dropdown menu - this will show your the default NIM connector.

If you do not see the blue model with the button as show in the below images, your system is not compatible with running a NIM. Please see the system requirements for more information.

Fresh install
If you have never run the NVIDIA NIM installer before, you will see the following screen:


Post install
If you have already run the NVIDIA NIM installer before or otherwise have all of the NIM pre-requisites installed, you will see the following screen:


You can see the blue button has changed to "Swap to Managed Mode" and you can click on it to enable managed mode.

Running the NIM Installer
This step only needs to be run once per machine. Once NVIDIA NIM is installed, you will not need to run the installer ever again.

See Swap to Managed Mode for more information on how to use NVIDIA NIM in managed mode.

If you encounter any issues with the NIM installer you can get help from NVIDIA via: - NVIDIA NIM Community Forums - Technical Support - [NVIDIA NIM AI RTX PC Discord

General Discussion & Announcements](https://discord.gg/nvidiadeveloper)
The official NVIDIA NIM installer is a pre-built binary that runs in the AnythingLLM Desktop client built by NVIDIA. If your system or GPU is not compatible with running a NIM, you will see an error message during this step and will be unable to run a NIM on AnythingLLM or your system in general.

Clicking on the "Run NVIDIA NIM Installer" button will prompt your to run the NIM installer as a separate window.

If you want to run the NIM installer manually, you can download the installer from NVIDIA directly via their WSL2 docs.


Click through the installer and follow the instructions to install NVIDIA NIM. This process will take a few minutes to complete and may require a restart of your machine post-installation.


Swap to Managed Mode
After closing the completed NIM installer, you will see the blue button change to "Swap to Managed Mode". Clicking on this button will allow AnythingLLM to manage your NIM models for you via a simple UI.


This is the recommended mode of operation for AnythingLLM as it will allow you to easily update your NIM models and manage your NIM instances. Once you have swapped to managed mode, you will see the NIM manager UI with no models.


Installing your first model
To install your first model, click on the "Import NIM from NVIDIA" button in the NIM manager UI at the top of the screen.

Here you will see a short list of pre-selected and recommended models for you to choose from. Clicking on any of the models will begin the download process after prompting a short license agreement dialog.


You can however select any model from the NVIDIA NIM catalog and paste it's model ID into the input field and click "Pull Model" to install it - however this is not recommended.

Monitoring your model download
NIM models are more than just a single GGUF, which you may be used to from other LLM providers. NIM models are the model + software to run the model as fast as possible on your RTX GPU - so they can be a bit larger than your typical GGUF.

You can monitor the progress of the model download in the NIM manager UI by clicking on the blue text link below the the "Import NIM from NVIDIA" button. This will show you the live download progress.

The speed of the download will vary depending on your internet connection speed and the model you are downloading.

You can close this window at any time and it will not affect the download in any way.


You will see the text "Pulling image from NGC Registry Completed" when the model has finished downloading and is unpacked and ready to use.


Starting your first NIM
The very first time you start a NIM, it will take a few minutes to download additional model files start its inference service. This is normal and expected and subsequent starts will be much faster.

You can monitor the progress of the NIM starting in the NIM manager UI by clicking on the blue text link below the the "logs" button. This will show you the live startup progress.

Clicking on the "Refresh" button in the NIM manager UI will show you all of the NIMs you have installed. Models that have never been started will show a "Start NIM" button. You can click on this button to start the NIM.

This will begin the process of starting the NIM and you will see the NIM status change to "Starting NIM..." in the NIM manager UI as well as see VRAM begin to be allocated to the NIM.


Once the NIM has started, you will see the NIM status change to "NIM Started" as well as the ability to Stop and Delete the NIM and see its logs.


Streaming logs from the NIM
You can stream the logs from the NIM by clicking on the "Logs" button in the NIM manager UI. This will open a new tab with the NIM logs. You can close this window at any time and it will not affect the NIM in any way.


How do I know when my NIM is ready to use?
In the NIM logs, you will see the following message in the log output:

// a bunch of other logs
Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

This means that your NIM is ready to use! You can now start using it in AnythingLLM.

Selecting your NIM in AnythingLLM
To select your NIM in AnythingLLM, simply click on the model card for the NIM you want to use and click "Save changes" in the top right.


You can now use this model in AnythingLLM as you would any other model or provider.

Stopping your NIM
Since running a NIM will reserve VRAM on your GPU, we recommend that you stop your NIM when you are not using it. You can stop your NIM by clicking on the "Stop NIM" button in the NIM manager UI. This will begin the process of stopping the NIM and you will see the NIM status change to "Stopping NIM..." in the NIM manager UI as well as see VRAM begin to be deallocated from the NIM.

Closing AnythingLLM currently does not stop the NIM - so you will need to manually stop the NIM by clicking on the "Stop NIM" button in the NIM manager UI.

Deleting your NIM
You can delete your NIM by clicking on the "Delete NIM" button in the NIM manager UI. This will delete the NIM instance, but will not delete the model from your system. If you wish to delete the model from your system, you will need to do so manually via WSL.

wsl -d NVIDIA-Workbench
podman image ls # Will show you all of the images on your system
podman rmi <image_id> # Will delete the image from your system - the container should be deleted prior to this
This will delete the NIM image from your system totally.

Last updated on October 9, 2025
System Requirements
Attaching vs RAG
MIT 2025 © Mintplex Labs.
Walkthrough ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

What even is an agent?
Some LLMs are bad at generating JSON and even worse at following instructions.
Model is hallucinating a tool call.
Common Solutions
LLM says it cannot call XYZ tool.
Common Solutions
LLM is refusing to even detect or call a tool at all.
Common Solutions
Edit this page
Scroll to top
AI Agent not using tools!
Why is my @agent not using tools!
AI Agents unlock new and exciting ways to use and leverage LLMs to do things for you as opposed to just reply with text. However, these LLMs are still not fully intelligent and like other implementations of LLMs - this method is not without its "gotchas".

Like other LLM problems, this mostly comes down to the model you are using and as always a more powerful & capable model yields better results. When using agents, we recommend the best model you can run.

caveat: There are some smaller models that are specifically trained for JSON/function calling and they can be used in lieu of just a larger model, but this has its own drawbacks when you want to then get the final response back as a normal chat. In general, you should use a general text/instruct model.

What even is an agent?
Without getting too technical there is some foundational knowledge to understand what an "AI Agent" even is. The below graphics really describe what LLMs are doing and "reasoning" about. As you can see, its no different that a specifically formatted text response!


So now that we know LLMs are basically doing an extra step in between your prompt and it's final answer, any agent's implementation usually goes wrong in the JSON generation part.

Okay, so now that we know how this pipeline works in order for an agent to even function works, how can we solve and debug issues?

Some LLMs are bad at generating JSON and even worse at following instructions.
Tip: Cloud based (un-quantized) models are typically dramatically better at following instructions and forming valid JSON matching the required tool-call.

You can use a cloud based model for just agent calls in AnythingLLM and use an open-source model for normal chatting.

The main issue we see with agents are people who want to use a smaller parameter model that is heavily quantized and want to get GPT-level quality tool interactions. Below are the reasons + ways to mitigate the effects of bad tool calls and their common solutions.

Model is hallucinating a tool call.
When a tool is actually called you will see what we call a "thought" output to the UI. This indicates that the tool was actually called. If the LLM responds with information and you don't see a thought-chain, it is likely making up the output and pretended to call a tool.


Common Solutions
Swap to a high quantization version or larger param model
/reset chat history and re-ask the prompt
LLM says it cannot call XYZ tool.
Some models are aligned too heavily and will refuse to use some tools because of their training. This is common for requests like website scraping.

Common Solutions
Swap to a high quantization version, larger param model, or less restricted model
/reset chat history and re-ask the prompt
Turn off tools you are not using to reduce prompt window size
LLM is refusing to even detect or call a tool at all.
Open-source models, with their quantization and limited context window are susceptible to just refusing to discover or call a tool properly.

When tools are injected into the LLMs prompt for discovery and execution they can quite often be "overloaded" with information or due to their quantization are unable to create valid JSON that exactly matches the schema required for a tool call to succeed. The LLM is simply generating JSON, something lower-param and quantized models are particularly bad at!

AnythingLLM however does make some significant corrections to have slightly invalid JSON be formatted properly so a call can succeed, but we can only do so much on this front.

Common Solutions
Swap to a high quantization version, larger param model, or less restricted model
/reset chat history and re-ask the prompt (chat history can sometimes impact output of JSON)
Turn off tools you are not using to reduce prompt window size and load on prompt.
Last updated on September 18, 2025
RAG in AnythingLLM
Ollama Connection Debugging
MIT 2025 © Mintplex Labs.
Why is my AI Agent not using tools! ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

General Troubleshooting (Desktop & Docker)
Ensure Ollama server is Running
Troubleshooting (Docker)
localhost and 127.0.0.1 do not work on Docker.
Troubleshooting (Remote Ollama)
AnythingLLM Cloud + Local Ollama
Edit this page
Scroll to top
Ollama Connection Debugging
Connecting to Ollama is a very simple process, but sometimes things can appear to not being working depending on if you are using the AnythingLLM Desktop version or running AnythingLLM via Docker.

In general, all AnythingLLM instances just need a valid URL to connect to Ollama running anywhere, however there can be some nuances depending on how you are running AnythingLLM or Ollama - in any case, all that is needed is a reachable URL to connect to Ollama.

The most common issue people run into is trying to use localhost or 127.0.0.1 to connect to Ollama running on their local machine when running AnythingLLM via Docker - see the Troubleshooting (Docker) section for how to fix this.

General Troubleshooting (Desktop & Docker)
On both the Desktop and Docker versions of AnythingLLM, the Ollama URL is automatically detected if we can detect it. If the Ollama URL is not detected, you will need to manually set the Ollama URL in the AnythingLLM settings.

The list of automatically detected URLs is as follows:

http://127.0.0.1:11434
http://host.docker.internal:11434
http://172.17.0.1:11434
If your Ollama URL is not detected because it is not in the list above, you will need to manually set the Ollama URL in the AnythingLLM settings - which will be shown in the UI for you to modify.

Ensure Ollama server is Running
Before attempting any fixes or URL changes, verify that Ollama is running properly on your device:

Open your web browser and navigate to http://127.0.0.1:11434
You should see a page similar to this:
Ollama running in background
If you don't see this page, troubleshoot your Ollama installation and ensure that it is running properly before moving forward as well as make sure you run the ollama serve command. Most of the time, Ollama will automatically start the server when ollama is running.

Running ollama run model-name will not start the server - this is only for running models in your command line and you will not be able to use the Ollama API with this command.

Troubleshooting (Docker)
If you are running AnythingLLM via Docker and you are trying to connect to Ollama running locally on your machine.

If you are seeing no models loaded in AnythingLLM or getting error responses from Ollama - 100% of the time this is beacause you are using the wrong URL in the connection in AnythingLLM.

localhost and 127.0.0.1 do not work on Docker.
On Docker, localhost and 127.0.0.1 are not valid URLs for the Docker container Ollama connection in AnythingLLM because both of these refer to the container network and not the host machine.

To fix this, you can use the host.docker.internal (Windows/MacOS) or 172.17.0.1 (Linux) URLs to connect to the host machine from the Docker container with the same port (default 11434).

Running Docker on Windows or MacOS (available since Docker version 18.03):

http://localhost:11434 => http://host.docker.internal:11434
http://127.0.0.1:11434 => http://host.docker.internal:11434
Running Docker on Linux:

http://localhost:11434 => http://172.17.0.1:11434
http://127.0.0.1:11434 => http://172.17.0.1:11434
Troubleshooting (Remote Ollama)
If you are running AnythingLLM via Docker and are trying to connect to Ollama running on another machine the underlying principle is the same where the Ollama URL is the IP address of the machine running Ollama.

In the case of a remote Ollama, the Ollama URL is the IP address of the machine running Ollama and it is your responsibility to ensure that the IP address is correct, your firewall rules are correct, and that the machine is running ollama. There is no way for AnythingLLM to automatically detect the IP address of the machine running Ollama.

AnythingLLM Cloud + Local Ollama
You cannot connect to Ollama running on your local machine when using AnythingLLM Cloud. This would require you to expose your local machine to the internet long-term via a service like ngrok which is not recommended and not secure.

While it is possible, we do not recommend it and it is your discretion to do so if you understand the security implications of SSH tunneling your local machine to the internet. We will not provide support for any issues related to exposing your local machine to the internet.

Last updated on September 18, 2025
AI Agent not using tools!
Fetch failed error on embed
MIT 2025 © Mintplex Labs.
General Help ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

What is this?
Check if the machine running AnythingLLM is blocking downloads from HuggingFace or AWS.
Why is this happening?
How to fix it?
Windows Visual C++ Redistributable
Why is this happening?
How to fix it?
Your CPU is not supported
Why is this happening?
How to fix it?
Edit this page
Scroll to top
Fetch failed error on embed
What is this?
When you try to embed a file in AnythingLLM, you might see a "Fetch failed" error. There are a few reasons why this might happen and all of them are fixable quite easily and are all related to the machine running AnythingLLM or firewall permissions.

Below are the most common fixes for this error ordered from the most likely to the least likely.

Check if the machine running AnythingLLM is blocking downloads from HuggingFace or AWS.
This error applies to you if:

 You are using the default AnythingLLM embedder model
 You may have a firewall blocking downloads from HuggingFace or AWS either by default or because you have a custom firewall installed by whoever manages your network.
Why is this happening?
This error happens when the machine running AnythingLLM is blocking downloads from HuggingFace or AWS. We do not pre-bundle the embedding model into the app, so the machine needs to download the model for its very first use. After it is downloaded, the model is cached so it doesn't need to be downloaded again. Your embeddings for the default embedder model are always done locally, this is just a problem with downloading the model GGUF and tokenizer.

How to fix it?
Check your storage folder and see if a folder named models/Xenova exists.
If this folder does not exist, it's likely that the machine is blocking downloads from HuggingFace or AWS.
Unblock the huggingface.co and api.huggingface.co domains on your machine.
Try embedding again.
Unblock this origin: https://cdn.anythingllm.com/support/models/
Try embedding again.
Still not working? Try the next solution.

Windows Visual C++ Redistributable
This error applies to you if:

 You are using the default AnythingLLM embedder model
 You are on Windows
Why is this happening?
This error happens when the machine running AnythingLLM is missing the Windows Visual C++ Redistributable. This is a library that is required to run the model.

How to fix it?
Download the Visual C++ Redistributable v14.x and install it.
Try embedding again.
Still not working? Try the next solution.

Your CPU is not supported
This error applies to you if:

 You are using the default AnythingLLM vector database
Why is this happening?
LanceDB is a vector database that is used to store the embeddings. It is the default vector database for AnythingLLM.

Your CPU is not supported if you are using a CPU that does not support AVX2.

How to fix it?
Use a machine with a supported CPU.
Use another vector database provider for vector storage. We support most of the popular vector databases.
Last updated on September 18, 2025
Ollama Connection Debugging
Manual QNN Model Download
MIT 2025 © Mintplex Labs.
'Fetch failed' error on embed ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

What is this?
Download the models
Once your zip file is downloaded
Edit this page
Scroll to top
Manual QNN Model Download
What is this?
Sometimes you need to download the NPU models manually due to connection issues. This is a manual process but it's quite simple to do and should only be done if you are unable to download the models automatically from selecting them in the GUI on the desktop app.

Download the models
You can download the models from the following links:

Llama-3.2-3B-Chat (8k context)
Llama-3.2-3B-Chat (16k context)
Llama-3.1-8B-Chat (8k context)
Phi 3.5-mini-instruct (4k context)
Once your zip file is downloaded
Open the models/QNN folder (or create it if it doesn't exist) in the desktop storage folder.
Move the zip file into this folder.
Extract the zip file.
You should now have a folder named with the same name as the zip file and inside it will be the model files.

# Example folder structure
models/QNN/
└── llama_v3_2_3b_chat_8k/
    ├── genie_config.json
    ├── htp_backend_etc.bin
    ├── related-model-bin-file.bin
    └── tokenizer.json
Restart the desktop app. Now the model should be available in the GUI to be selected and used for inference.
Last updated on September 18, 2025
Fetch failed error on embed
What are beta previews?
MIT 2025 © Mintplex Labs.
Manual QNN Model Download ~ AnythingLLMip to main content

Open WebUI
Blog
GitHub
Discord

Search Ctrl+K
🏡 Home
🚀 Getting Started

⭐ Features

Federated Authentication

Role-Based Access Control (RBAC)

Retrieval Augmented Generation (RAG)

Tools & Functions (Plugins)

Create & Edit Images

Speech-to-Text & Text-to-Speech

Web Search

Workspace

Chat Features

Interface

Channels
Evaluation
Model Context Protocol (MCP)
Notes
Pipelines

🛠️ Troubleshooting

🏢 Open WebUI for Enterprises

🎓 Tutorials

❓ FAQ
🛣️ Roadmap
🛡️ Security Policy
🤝 Contributing
💖 Sponsorships
🎨 Design Guidelines
⚖️ Open WebUI License
🎯 Our Mission
👥 Our Team
Sponsored by Open WebUI Inc.
Open WebUI Inc.
We are hiring! Shape the way humanity engages with intelligence.

⭐ Features
Sponsored by Open WebUI Inc.
Open WebUI Inc.
We are hiring! Shape the way humanity engages with intelligence.

Key Features of Open WebUI ⭐
🚀 Effortless Setup: Install seamlessly using Docker, Kubernetes, Podman, Helm Charts (kubectl, kustomize, podman, or helm) for a hassle-free experience with support for both :ollama image with bundled Ollama and :cuda with CUDA support.

🛠️ Guided Initial Setup: Complete the setup process with clarity, including an explicit indication of creating an admin account during the first-time setup.

🤝 OpenAI API Integration: Effortlessly integrate OpenAI-compatible APIs for versatile conversations alongside Ollama models. The OpenAI API URL can be customized to integrate Open WebUI seamlessly with various third-party applications.

🛡️ Granular Permissions and User Groups: By allowing administrators to create detailed user roles, user groups, and permissions across the workspace, we ensure a secure user environment for all users involved. This granularity not only enhances security, but also allows for customized user experiences, fostering a sense of ownership and responsibility amongst users.

🔐 SCIM 2.0 Provisioning: Enterprise-grade user and group provisioning through SCIM 2.0 protocol, enabling seamless integration with identity providers like Okta, Azure AD, and Google Workspace for automated user lifecycle management.

📱 Responsive Design: Enjoy a seamless experience across desktop PCs, laptops, and mobile devices.

📱 Progressive Web App for Mobile: Enjoy a native progressive web application experience on your mobile device with offline access on localhost or a personal domain, and a smooth user interface. In order for our PWA to be installable on your device, it must be delivered in a secure context. This usually means that it must be served over HTTPS.

info
To set up a PWA, you'll need some understanding of technologies like Linux, Docker, and reverse proxies such as Nginx, Caddy, or Traefik. Using these tools can help streamline the process of building and deploying a PWA tailored to your needs. While there's no "one-click install" option available, and your available option to securely deploy your Open WebUI instance over HTTPS requires user experience, using these resources can make it easier to create and deploy a PWA tailored to your needs.
✒️🔢 Full Markdown and LaTeX Support: Elevate your LLM experience with comprehensive Markdown, LaTex, and Rich Text capabilities for enriched interaction.

🧩 Model Builder: Easily create custom models from base Ollama models directly from Open WebUI. Create and add custom characters and agents, customize model elements, and import models effortlessly through Open WebUI Community integration.

📚 Advanced RAG Integration with Multiple Vector Databases: Dive into the future of chat interactions with cutting-edge Retrieval Augmented Generation (RAG) technology. Choose from 9 vector database options: ChromaDB (default), PostgreSQL with PGVector, Qdrant, Milvus, Elasticsearch, OpenSearch, Pinecone, S3Vector, and Oracle 23ai. Documents can be loaded into the Documents tab of the Workspace and accessed using the pound key [#] before a query, or by starting the prompt with [#] followed by a URL for webpage content integration.

📄 Advanced Document Extraction with Multiple Engines: Extract text and data from various document formats including PDFs, Word documents, Excel spreadsheets, PowerPoint presentations, and more using your choice of extraction engines: Apache Tika, Docling, Azure Document Intelligence, Mistral OCR, or external custom (self-built) content extraction engines/document loaders. Advanced document processing capabilities enable seamless integration with your knowledge base, preserving structure and formatting while supporting OCR for scanned documents and images.

🔍 Web Search for RAG with 15+ Providers: Perform web searches using 15+ providers including SearXNG, Google PSE, Brave Search, Kagi, Mojeek, Bocha, Tavily, Perplexity (AI models and Search API), serpstack, serper, Serply, DuckDuckGo, SearchAPI, SerpApi, Bing, Jina, Exa, Sougou, Azure AI Search, and Ollama Cloud, injecting results directly into your local Retrieval Augmented Generation (RAG) experience.

🌐 Web Browsing Capabilities: Integrate websites seamlessly into your chat experience by using the # command followed by a URL. This feature enables the incorporation of web content directly into your conversations, thereby enhancing the richness and depth of your interactions.

🎨 Image Generation & Editing Integration: Seamlessly create and edit images using multiple engines including OpenAI's DALL-E (generation and editing), Gemini (generation and editing), ComfyUI (local, generation and editing), and AUTOMATIC1111 (local, generation). Support for both text-to-image generation and prompt-based image editing workflows with dynamic visual content.

⚙️ Concurrent Model Utilization: Effortlessly engage with multiple models simultaneously, harnessing their unique strengths for optimal responses. Leverage a diverse set of model modalities in parallel to enhance your experience.

🔐 Role-Based Access Control (RBAC): Ensure secure access with restricted permissions. Only authorized individuals can access your Ollama, while model creation and pulling rights are exclusively reserved for administrators.

🌐🌍 Multilingual Support: Experience Open WebUI in your preferred language with our internationalization (i18n) support. We invite you to join us in expanding our supported languages! We're actively seeking contributors!

💾 Persistent Artifact Storage: Built-in key-value storage API for artifacts, enabling features like journals, trackers, leaderboards, and collaborative tools with both personal and shared data scopes that persist across sessions.

☁️ Cloud Storage Integration: Native support for cloud storage backends including Amazon S3 (with S3-compatible providers), Google Cloud Storage, and Microsoft Azure Blob Storage for scalable file storage and data management.

☁️ Enterprise Cloud Integration: Seamlessly import documents from Google Drive and OneDrive/SharePoint directly through the file picker interface, enabling smooth workflows with enterprise cloud storage solutions.

📊 Production Observability with OpenTelemetry: Built-in OpenTelemetry support for comprehensive monitoring with traces, metrics, and logs export to your existing observability stack (Prometheus, Grafana, Jaeger, etc.), enabling production-grade monitoring and debugging.

🔒 Encrypted Database Support: Optional at-rest encryption for SQLite databases using SQLCipher, providing enhanced security for sensitive data in smaller deployments without requiring PostgreSQL infrastructure.

⚖️ Horizontal Scalability for Production: Redis-backed session management and WebSocket support enabling multi-worker and multi-node deployments behind load balancers for high-availability production environments.

🌟 Continuous Updates: We are committed to improving Open WebUI with regular updates, fixes, and new features.

And many more remarkable features including... ⚡️
🔧 Pipelines Support
🔧 Pipelines Framework: Seamlessly integrate and customize your Open WebUI experience with our modular plugin framework for enhanced customization and functionality (https://github.com/open-webui/pipelines). Our framework allows for the easy addition of custom logic and integration of Python libraries, from AI agents to home automation APIs.

📥 Upload Pipeline: Pipelines can be uploaded directly from the Admin Panel > Settings > Pipelines menu, streamlining the pipeline management process.

The possibilities with our Pipelines framework knows no bounds and are practically limitless. Start with a few pre-built pipelines to help you get started!
🔗 Function Calling: Integrate Function Calling seamlessly through Pipelines to enhance your LLM interactions with advanced function calling capabilities.

📚 Custom RAG: Integrate a custom Retrieval Augmented Generation (RAG) pipeline seamlessly to enhance your LLM interactions with custom RAG logic.

📊 Message Monitoring with Langfuse: Monitor and analyze message interactions in real-time usage statistics via Langfuse pipeline.

⚖️ User Rate Limiting: Manage API usage efficiently by controlling the flow of requests sent to LLMs to prevent exceeding rate limits with Rate Limit pipeline.

🌍 Real-Time LibreTranslate Translation: Integrate real-time translations into your LLM interactions using LibreTranslate pipeline, enabling cross-lingual communication.

Please note that this pipeline requires further setup with LibreTranslate in a Docker container to work.
🛡️ Toxic Message Filtering: Our Detoxify pipeline automatically filters out toxic messages to maintain a clean and safe chat environment.

🔒 LLM-Guard: Ensure secure LLM interactions with LLM-Guard pipeline, featuring a Prompt Injection Scanner that detects and mitigates crafty input manipulations targeting large language models. This protects your LLMs from data leakage and adds a layer of resistance against prompt injection attacks.

🕒 Conversation Turn Limits: Improve interaction management by setting limits on conversation turns with Conversation Turn Limit pipeline.

📈 OpenAI Generation Stats: Our OpenAI pipeline provides detailed generation statistics for OpenAI models.

🚀 Multi-Model Support: Our seamless integration with various AI models from various providers expands your possibilities with a wide range of language models to select from and interact with.

In addition to the extensive features and customization options, we also provide a library of example pipelines ready to use along with a practical example scaffold pipeline to help you get started. These resources will streamline your development process and enable you to quickly create powerful LLM interactions using Pipelines and Python. Happy coding! 💡
🖥️ User Experience
🖥️ Intuitive Interface: The chat interface has been designed with the user in mind, drawing inspiration from the user interface of ChatGPT.

⚡ Swift Responsiveness: Enjoy reliably fast and responsive performance.

🎨 Splash Screen: A simple loading splash screen for a smoother user experience.

🌐 Personalized Interface: Choose between a freshly designed search landing page and the classic chat UI from Settings > Interface, allowing for a tailored experience.

📦 Pip Install Method: Installation of Open WebUI can be accomplished via the command pip install open-webui, which streamlines the process and makes it more accessible to new users. For further information, please visit: https://pypi.org/project/open-webui/.

🌈 Theme Customization: Personalize your Open WebUI experience with a range of options, including a variety of solid, yet sleek themes, customizable chat background images, and three mode options: Light, Dark, or OLED Dark mode - or let Her choose for you! ;)

🖼️ Custom Background Support: Set a custom background from Settings > Interface to personalize your experience.

📝 Rich Banners with Markdown: Create visually engaging announcements with markdown support in banners, enabling richer and more dynamic content.

💻 Code Syntax Highlighting: Our syntax highlighting feature enhances code readability, providing a clear and concise view of your code.

🗨️ Markdown Rendering in User Messages: User messages are now rendered in Markdown, enhancing readability and interaction.

🎨 Flexible Text Input Options: Switch between rich text input and legacy text area input for chat, catering to user preferences and providing a choice between advanced formatting and simpler text input.

👆 Effortless Code Sharing : Streamline the sharing and collaboration process with convenient code copying options, including a floating copy button in code blocks and click-to-copy functionality from code spans, saving time and reducing frustration.

🎨 Interactive Artifacts: Render web content and SVGs directly in the interface, supporting quick iterations and live changes for enhanced creativity and productivity.

🖊️ Live Code Editing: Supercharged code blocks allow live editing directly in the LLM response, with live reloads supported by artifacts, streamlining coding and testing.

🔍 Enhanced SVG Interaction: Pan and zoom capabilities for SVG images, including Mermaid diagrams, enable deeper exploration and understanding of complex concepts.

🔍 Text Select Quick Actions: Floating buttons appear when text is highlighted in LLM responses, offering deeper interactions like "Ask a Question" or "Explain", and enhancing overall user experience.

↕️ Bi-Directional Chat Support: You can easily switch between left-to-right and right-to-left chat directions to accommodate various language preferences.

📱 Mobile Accessibility: The sidebar can be opened and closed on mobile devices with a simple swipe gesture.

🤳 Haptic Feedback on Supported Devices: Android devices support haptic feedback for an immersive tactile experience during certain interactions.

🔍 User Settings Search: Quickly search for settings fields, improving ease of use and navigation.

📜 Offline Swagger Documentation: Access developer-friendly Swagger API documentation offline, ensuring full accessibility wherever you are.

💾 Performance Optimizations: Lazy loading of large dependencies minimizes initial memory usage, boosting performance and reducing loading times.

🚀 Persistent and Scalable Configuration: Open WebUI configurations are stored in a database (webui.db), allowing for seamless load balancing, high-availability setups, and persistent settings across multiple instances, making it easy to access and reuse your configurations.

🔄 Portable Import/Export: Easily import and export Open WebUI configurations, simplifying the process of replicating settings across multiple systems.

❓ Quick Access to Documentation & Shortcuts: The question mark button located at the bottom right-hand corner of the main UI screen (available on larger screens like desktop PCs and laptops) provides users with easy access to the Open WebUI documentation page and available keyboard shortcuts.

📜 Changelog & Check for Updates: Users can access a comprehensive changelog and check for updates in the Settings > About > See What's New menu, which provides a quick overview of the latest features, improvements, and bug fixes, as well as the ability to check for updates.

💬 Conversations
💬 True Asynchronous Chat: Enjoy uninterrupted multitasking with true asynchronous chat support, allowing you to create chats, navigate away, and return anytime with responses ready.

🔔 Chat Completion Notifications: Stay updated with instant in-UI notifications when a chat finishes in a non-active tab, ensuring you never miss a completed response.

🌐 Notification Webhook Integration: Receive timely updates for long-running chats or external integration needs with configurable webhook notifications, even when your tab is closed.

📚 Channels (Beta): Explore real-time collaboration between users and AIs with Discord/Slack-style chat rooms, build bots for channels, and unlock asynchronous communication for proactive multi-agent workflows.

🖊️ Typing Indicators in Channels: Enhance collaboration with real-time typing indicators in channels, keeping everyone engaged and informed.

👤 User Status Indicators: Quickly view a user's status by clicking their profile image in channels, providing better coordination and availability insights.

💬 Chat Controls: Easily adjust parameters for each chat session, offering more precise control over your interactions.

💖 Favorite Response Management: Easily mark and organize favorite responses directly from the chat overview, enhancing ease of retrieval and access to preferred responses.

📌 Pinned Chats: Support for pinned chats, allowing you to keep important conversations easily accessible.

🔍 RAG Embedding Support: Change the Retrieval Augmented Generation (RAG) embedding model directly in the Admin Panel > Settings > Documents menu, enhancing document processing. This feature supports Ollama and OpenAI models.

📜 Citations in RAG Feature: The Retrieval Augmented Generation (RAG) feature allows users to easily track the context of documents fed to LLMs with added citations for reference points.

🌟 Enhanced RAG Pipeline: A togglable hybrid search sub-feature for our RAG embedding feature that enhances the RAG functionality via BM25, with re-ranking powered by CrossEncoder, and configurable relevance score thresholds.

📹 YouTube RAG Pipeline: The dedicated Retrieval Augmented Generation (RAG) pipeline for summarizing YouTube videos via video URLs enables smooth interaction with video transcriptions directly.

📁 Comprehensive Document Retrieval: Toggle between full document retrieval and traditional snippets, enabling comprehensive tasks like summarization and supporting enhanced document capabilities.

🌟 RAG Citation Relevance: Easily assess citation accuracy with the addition of relevance percentages in RAG results.

🗂️ Advanced RAG: Improve RAG accuracy with smart pre-processing of chat history to determine the best queries before retrieval.

📚 Inline Citations for RAG: Benefit from seamless inline citations for Retrieval-Augmented Generation (RAG) responses, improving traceability and providing source clarity for newly uploaded files.

📁 Large Text Handling: Optionally convert large pasted text into a file upload to be used directly with RAG, keeping the chat interface cleaner.

🔄 Multi-Modal Support: Effortlessly engage with models that support multi-modal interactions, including images (e.g., LLaVA).

🤖 Multiple Model Support: Quickly switch between different models for diverse chat interactions.

🔀 Merge Responses in Many Model Chat: Enhances the dialogue by merging responses from multiple models into a single, coherent reply.

✅ Multiple Instances of Same Model in Chats: Enhanced many model chat to support adding multiple instances of the same model.

💬 Temporary Chat Feature: Introduced a temporary chat feature, deprecating the old chat history setting to enhance user interaction flexibility.

🖋️ User Message Editing: Enhanced the user chat editing feature to allow saving changes without sending.

💬 Efficient Conversation Editing: Create new message pairs quickly and intuitively using the Cmd/Ctrl+Shift+Enter shortcut, streamlining conversation length tests.

🖼️ Client-Side Image Compression: Save bandwidth and improve performance with client-side image compression, allowing you to compress images before upload from Settings > Interface.

👥 '@' Model Integration: By seamlessly switching to any accessible local or external model during conversations, users can harness the collective intelligence of multiple models in a single chat. This can done by using the @ command to specify the model by name within a chat.

🏷️ Conversation Tagging : Effortlessly categorize and locate tagged chats for quick reference and streamlined data collection using our efficient 'tag:' query system, allowing you to manage, search, and organize your conversations without cluttering the interface.

🧠 Auto-Tagging: Conversations can optionally be automatically tagged for improved organization, mirroring the efficiency of auto-generated titles.

👶 Chat Cloning: Easily clone and save a snapshot of any chat for future reference or continuation. This feature makes it easy to pick up where you left off or share your session with others. To create a copy of your chat, simply click on the Clone button in the chat's dropdown options. Can you keep up with your clones?

⭐ Visualized Conversation Flows: Interactive messages diagram for improved visualization of conversation flows, enhancing understanding and navigation of complex discussions.

📁 Chat Folders: Organize your chats into folders, drag and drop them for easy management, and export them seamlessly for sharing or analysis.

📤 Easy Chat Import: Import chats into your workspace by simply dragging and dropping chat exports (JSON) onto the sidebar.

📜 Prompt Preset Support: Instantly access custom preset prompts using the / command in the chat input. Load predefined conversation starters effortlessly and expedite your interactions. Import prompts with ease through Open WebUI Community integration or create your own!

📅 Prompt Variables Support: Prompt variables such as {{CLIPBOARD}}, {{CURRENT_DATE}}, {{CURRENT_DATETIME}}, {{CURRENT_TIME}}, {{CURRENT_TIMEZONE}}, {{CURRENT_WEEKDAY}}, {{USER_NAME}}, {{USER_LANGUAGE}}, and {{USER_LOCATION}} can be utilized in the system prompt or by using a slash command to select a prompt directly within a chat.

Please note that the {{USER_LOCATION}} prompt variable requires a secure connection over HTTPS. To utilize this particular prompt variable, please ensure that {{USER_LOCATION}} is toggled on from the Settings > Interface menu.
Please note that the {{CLIPBOARD}} prompt variables requires access to your device's clipboard.
🧠 Memory Feature: Manually add information you want your LLMs to remember via the Settings > Personalization > Memory menu. Memories can be added, edited, and deleted.

💻 Model Management
🛠️ Model Builder: All models can be built and edited with a persistent model builder mode within the models edit page.

📚 Knowledge Support for Models: The ability to attach tools, functions, and knowledge collections directly to models from a model's edit page, enhancing the information available to each model.

🗂️ Model Presets: Create and manage model presets for both the Ollama and OpenAI API.

🏷️ Model Tagging: The models workspace enables users to organize their models using tagging.

📋 Model Selector Dropdown Ordering: Models can be effortlessly organized by dragging and dropping them into desired positions within the model workspace, which will then reflect the changes in the model dropdown menu.

🔍 Model Selector Dropdown: Easily find and select your models with fuzzy search and detailed model information with model tags and model descriptions.

⌨️ Arrow Keys Model Selection: Use arrow keys for quicker model selection, enhancing accessibility.

🔧 Quick Actions in Model Workspace: Enhanced Shift key quick actions for hiding/displaying and deleting models in the model workspace.

😄 Transparent Model Usage: Stay informed about the system's state during queries with knowledge-augmented models, thanks to visible status displays.

⚙️ Fine-Tuned Control with Advanced Parameters: Gain a deeper level of control by adjusting model parameters such as seed, temperature, frequency penalty, context length, seed, and more.

🔄 Seamless Integration: Copy any ollama run {model:tag} CLI command directly from a model's page on Ollama library and paste it into the model dropdown to easily select and pull models.

🗂️ Create Ollama Modelfile: To create a model file for Ollama, navigate to the Admin Panel > Settings > Models > Create a model menu.

⬆️ GGUF File Model Creation: Effortlessly create Ollama models by uploading GGUF files directly from Open WebUI from the Admin Settings > Settings > Model > Experimental menu. The process has been streamlined with the option to upload from your machine or download GGUF files from Hugging Face.

⚙️ Default Model Setting: The default model preference for new chats can be set in the Settings > Interface menu on mobile devices, or can more easily be set in a new chat under the model selector dropdown on desktop PCs and laptops.

💡 LLM Response Insights: Details of every generated response can be viewed, including external model API insights and comprehensive local model info.

🕒 Model Details at a Glance: View critical model details, including model hash and last modified timestamp, directly in the Models workspace for enhanced tracking and management.

📥🗑️ Download/Delete Models: Models can be downloaded or deleted directly from Open WebUI with ease.

🔄 Update All Ollama Models: A convenient button allows users to update all their locally installed models in one operation, streamlining model management.

🍻 TavernAI Character Card Integration: Experience enhanced visual storytelling with TavernAI Character Card Integration in our model builder. Users can seamlessly incorporate TavernAI character card PNGs directly into their model files, creating a more immersive and engaging user experience.

🎲 Model Playground (Beta): Try out models with the model playground area (beta), which enables users to test and explore model capabilities and parameters with ease in a sandbox environment before deployment in a live chat environment.

👥 Collaboration
🗨️ Local Chat Sharing: Generate and share chat links between users in an efficient and seamless manner, thereby enhancing collaboration and communication.

👍👎 RLHF Annotation: Enhance the impact of your messages by rating them with either a thumbs up or thumbs down AMD provide a rating for the response on a scale of 1-10, followed by the option to provide textual feedback, facilitating the creation of datasets for Reinforcement Learning from Human Feedback (RLHF). Utilize your messages to train or fine-tune models, all while ensuring the confidentiality of locally saved data.

🔧 Comprehensive Feedback Export: Export feedback history data to JSON for seamless integration with RLHF processing and further analysis, providing valuable insights for improvement.

🤝 Community Sharing: Share your chat sessions with the Open WebUI Community by clicking the Share to Open WebUI Community button. This feature allows you to engage with other users and collaborate on the platform.

To utilize this feature, please sign-in to your Open WebUI Community account. Sharing your chats fosters a vibrant community, encourages knowledge sharing, and facilitates joint problem-solving. Please note that community sharing of chat sessions is an optional feature. Only Admins can toggle this feature on or off in the Admin Settings > Settings > General menu.
🏆 Community Leaderboard: Compete and track your performance in real-time with our leaderboard system, which utilizes the ELO rating system and allows for optional sharing of feedback history.

⚔️ Model Evaluation Arena: Conduct blind A/B testing of models directly from the Admin Settings for a true side-by-side comparison, making it easier to find the best model for your needs.

🎯 Topic-Based Rankings: Discover more accurate rankings with our experimental topic-based re-ranking system, which adjusts leaderboard standings based on tag similarity in feedback.

📂 Unified and Collaborative Workspace : Access and manage all your model files, prompts, documents, tools, and functions in one convenient location, while also enabling multiple users to collaborate and contribute to models, knowledge, prompts, or tools, streamlining your workflow and enhancing teamwork.

📚 History & Archive
📜 Chat History: Access and manage your conversation history with ease via the chat navigation sidebar. Toggle off chat history in the Settings > Chats menu to prevent chat history from being created with new interactions.

🔄 Regeneration History Access: Easily revisit and explore your entire LLM response regeneration history.

📬 Archive Chats: Effortlessly store away completed conversations you've had with models for future reference or interaction, maintaining a tidy and clutter-free chat interface.

🗃️ Archive All Chats: This feature allows you to quickly archive all of your chats at once.

📦 Export All Archived Chats as JSON: This feature enables users to easily export all their archived chats in a single JSON file, which can be used for backup or transfer purposes.

📄 Download Chats as JSON/PDF/TXT: Easily download your chats individually in your preferred format of .json, .pdf, or .txt format.

📤📥 Import/Export Chat History: Seamlessly move your chat data in and out of the platform via Import Chats and Export Chats options.

🗑️ Delete All Chats: This option allows you to permanently delete all of your chats, ensuring a fresh start.

🎙️ Audio, Voice, & Accessibility
🗣️ Voice Input Support with Multiple Providers: Engage with your model through voice interactions using multiple Speech-to-Text providers: Local Whisper (default, with VAD filtering), OpenAI-compatible endpoints, Deepgram, and Azure Speech Services. Enjoy the convenience of talking to your model directly with automatic voice input after 3 seconds of silence for a streamlined experience.

Microphone access requires manually setting up a secure connection over HTTPS to work, or manually whitelisting your URL at your own risk.
😊 Emoji Call: Toggle this feature on from the Settings > Interface menu, allowing LLMs to express emotions using emojis during voice calls for a more dynamic interaction.

Microphone access requires manually setting up a secure connection over HTTPS to work, or manually whitelisting your URL at your own risk.
🎙️ Hands-Free Voice Call Feature: Initiate voice calls without needing to use your hands, making interactions more seamless.

Microphone access requires manually setting up a secure connection over HTTPS to work, or manually whitelisting your URL at your own risk.
📹 Video Call Feature: Enable video calls with supported vision models like LlaVA and GPT-4o, adding a visual dimension to your communications.

Both Camera & Microphone access is required using a secure connection over HTTPS for this feature to work, or manually whitelisting your URL at your own risk.
👆 Tap to Interrupt: Stop the AI’s speech during voice conversations with a simple tap on mobile devices, ensuring seamless control over the interaction.

🎙️ Voice Interrupt: Stop the AI’s speech during voice conversations with your voice on mobile devices, ensuring seamless control over the interaction.

🔊 Multiple Text-to-Speech Providers: Customize your Text-to-Speech experience with multiple providers: OpenAI-compatible endpoints, Azure Speech Services, ElevenLabs (with EU residency support), local Transformers models, and browser-based WebAPI for reading aloud LLM responses.

🔗 Direct Call Mode Access: Activate call mode directly from a URL, providing a convenient shortcut for mobile device users.

✨ Customizable Text-to-Speech: Control how message content is segmented for Text-to-Speech (TTS) generation requests, allowing for flexible speech output options.

🔊 Azure Speech Services Integration: Supports Azure Speech services for Text-to-Speech (TTS), providing users with a wider range of speech synthesis options.

🎚️ Customizable Audio Playback: Allows users to adjust audio playback speed to their preferences in Call mode settings, enhancing accessibility and usability.

🎵 Broad Audio Compatibility: Enjoy support for a wide range of audio file format transcriptions with RAG, including 'audio/x-m4a', to broaden compatibility with audio content within the platform.

🎤 Deepgram Speech-to-Text Integration: Leverage Deepgram's advanced speech recognition capabilities for high-accuracy voice transcription, providing an additional STT option beyond local Whisper and OpenAI.

🔊 ElevenLabs Text-to-Speech Integration: Access ElevenLabs' premium voice synthesis with support for EU residency API endpoints, offering high-quality and natural-sounding voice output for enhanced user experiences.

🔊 Audio Compression: Experimental audio compression allows navigating around the 25MB limit for OpenAI's speech-to-text processing, expanding the possibilities for audio-based interactions.

🗣️ Experimental SpeechT5 TTS: Enjoy local SpeechT5 support for improved text-to-speech capabilities.

🐍 Code Execution
🚀 Versatile, UI-Agnostic, OpenAI-Compatible Plugin Framework: Seamlessly integrate and customize Open WebUI Pipelines for efficient data processing and model training, ensuring ultimate flexibility and scalability.

🛠️ Native Python Function Calling: Access the power of Python directly within Open WebUI with native function calling. Easily integrate custom code to build unique features like custom RAG pipelines, web search tools, and even agent-like actions via a built-in code editor to seamlessly develop and integrate function code within the Tools and Functions workspace.

🐍 Python Code Execution: Execute Python code locally in the browser via Pyodide with a range of libraries supported by Pyodide.

🌊 Mermaid Rendering: Create visually appealing diagrams and flowcharts directly within Open WebUI using the Mermaid Diagramming and charting tool, which supports Mermaid syntax rendering.

🔗 Iframe Support: Enables rendering HTML directly into your chat interface using functions and tools.

🔒 Integration & Security
✨ Multiple OpenAI-Compatible API Support: Seamlessly integrate and customize various OpenAI-compatible APIs, enhancing the versatility of your chat interactions.

🔑 Simplified API Key Management: Easily generate and manage secret keys to leverage Open WebUI with OpenAI libraries, streamlining integration and development.

🌐 HTTP/S Proxy Support: Configure network settings easily using the http_proxy or https_proxy environment variable. These variables, if set, should contain the URLs for HTTP and HTTPS proxies, respectively.

🌐🔗 External Ollama Server Connectivity: Seamlessly link to an external Ollama server hosted on a different address by configuring the environment variable.

🛢️ Flexible Database Integration: Seamlessly connect to custom databases, including SQLite, Postgres, and multiple vector databases like Milvus, using environment variables for flexible and scalable data management.

🗄️ Multiple Vector Database Support: Choose from 9 vector database options for optimal RAG performance: ChromaDB (default), PostgreSQL with PGVector, Qdrant, Milvus, Elasticsearch, OpenSearch, Pinecone, S3Vector, and Oracle 23ai. Each option provides different scaling characteristics and performance profiles to match your deployment needs.

☁️ Enterprise Cloud Storage Backends: Configure cloud storage backends including Amazon S3 (with S3-compatible providers like MinIO), Google Cloud Storage, and Microsoft Azure Blob Storage for scalable file storage, enabling stateless instances and distributed deployments.

📂 Cloud File Picker Integration: Import documents directly from Google Drive and OneDrive/SharePoint through native file picker interfaces, streamlining workflows for users working with enterprise cloud storage solutions.

🌐🗣️ External Speech-to-Text Support: The addition of external speech-to-text (STT) services provides enhanced flexibility, allowing users to choose their preferred provider for seamless interaction.

🌐 Remote ChromaDB Support: Extend the capabilities of your database by connecting to remote ChromaDB servers.

🔀 Multiple Ollama Instance Load Balancing: Effortlessly distribute chat requests across multiple Ollama instances for enhanced performance and reliability.

🚀 Advanced Load Balancing and Reliability: Utilize enhanced load balancing capabilities, stateless instances with full Redis support, and automatic web socket re-connection to promote better performance, reliability, and scalability in WebUI, ensuring seamless and uninterrupted interactions across multiple instances.

☁️ Cloud Storage Backend Support: Enable stateless Open WebUI instances with cloud storage backends (Amazon S3, Google Cloud Storage, Microsoft Azure Blob Storage) for enhanced scalability, high availability, and balancing heavy workloads across multiple instances.

🛠️ OAuth Management for User Groups: Enhance control and scalability in collaborative environments with group-level management via OAuth integration.

🔐 SCIM 2.0 Automated Provisioning: Enterprise-grade user and group provisioning through SCIM 2.0 protocol, enabling seamless integration with identity providers like Okta, Azure AD, and Google Workspace for automated user lifecycle management, reducing administrative overhead.

📊 OpenTelemetry Observability: Export traces, metrics, and logs to your observability stack using OpenTelemetry protocol (OTLP), supporting both gRPC and HTTP exporters with configurable endpoints, authentication, and sampling strategies for comprehensive production monitoring.

👑 Administration
👑 Super Admin Assignment: Automatically assigns the first sign-up as a super admin with an unchangeable role that cannot be modified by anyone else, not even other admins.

🛡️ Granular User Permissions: Restrict user actions and access with customizable role-based permissions, ensuring that only authorized individuals can perform specific tasks.

👥 Multi-User Management: Intuitive admin panel with pagination allows you to seamlessly manage multiple users, streamlining user administration and simplifying user life-cycle management.

🔧 Admin Panel: The user management system is designed to streamline the on-boarding and management of users, offering the option to add users directly or in bulk via CSV import.

👥 Active Users Indicator: Monitor the number of active users and which models are being utilized by whom to assist in gauging when performance may be impacted due to a high number of users.

🔒 Default Sign-Up Role: Specify the default role for new sign-ups to pending, user, or admin, providing flexibility in managing user permissions and access levels for new users.

🔒 Prevent New Sign-Ups: Enable the option to disable new user sign-ups, restricting access to the platform and maintaining a fixed number of users.

🔒 Prevent Chat Deletion: Ability for admins to toggle a setting that prevents all users from deleting their chat messages, ensuring that all chat messages are retained for audit or compliance purposes.

🔗 Webhook Integration: Subscribe to new user sign-up events via webhook (compatible with Discord, Google Chat, Slack and Microsoft Teams), providing real-time notifications and automation capabilities.

📣 Configurable Notification Banners: Admins can create customizable banners with persistence in config.json, featuring options for content, background color (info, warning, error, or success), and dismissibility. Banners are accessible only to logged-in users, ensuring the confidentiality of sensitive information.

🛡️ Model Whitelisting: Enhance security and access control by allowing admins to whitelist models for users with the user role, ensuring that only authorized models can be accessed.

🔑 Admin Control for Community Sharing: Admins can enable or disable community sharing for all users via a toggle in the Admin Panel > Settings menu. This toggle allows admins to manage accessibility and privacy, ensuring a secure environment. Admins have the option of enabling or disabling the Share on Community button for all users, which allows them to control community engagement and collaboration.

📧 Trusted Email Authentication: Optionally authenticate using a trusted email header, adding an extra layer of security and authentication to protect your Open WebUI instance.

🔒 Backend Reverse Proxy Support: Bolster security through direct communication between Open WebUI's backend and Ollama. This key feature eliminates the need to expose Ollama over the local area network (LAN). Requests made to the /ollama/api route from Open WebUI are seamlessly redirected to Ollama from the backend, enhancing overall system security and providing an additional layer of protection.

🔒 Authentication: Please note that Open WebUI does not natively support federated authentication schemes such as SSO, OAuth, SAML, or OIDC. However, it can be configured to delegate authentication to an authenticating reverse proxy, effectively achieving a Single Sign-On (SSO) experience. This setup allows you to centralize user authentication and management, enhancing security and user convenience. By integrating Open WebUI with an authenticating reverse proxy, you can leverage existing authentication systems and streamline user access to Open WebUI. For more information on configuring this feature, please refer to the Federated Authentication Support.

🔓 Optional Authentication: Enjoy the flexibility of disabling authentication by setting WEBUI_AUTH to False. This is an ideal solution for fresh installations without existing users or can be useful for demonstration purposes.

🚫 Advanced API Security: Block API users based on customized model filters, enhancing security and control over API access.

❗ Administrator Updates: Ensure administrators stay informed with immediate update notifications upon login, keeping them up-to-date on the latest changes and system statuses.

👥 User Group Management: Create and manage user groups for seamless organization and control.

🔐 Group-Based Access Control: Set granular access to models, knowledge, prompts, and tools based on user groups, allowing for more controlled and secure environments.

🛠️ Granular User Permissions: Easily manage workspace permissions, including file uploads, deletions, edits, and temporary chats, as well as model, knowledge, prompt, and tool creation.

🔑 LDAP Authentication: Enhance security and scalability with LDAP support for user management.

🔐 SCIM 2.0 Provisioning: Automate user and group lifecycle management through SCIM 2.0 protocol integration with identity providers like Okta, Azure AD, and Google Workspace, reducing administrative overhead and ensuring synchronized user management across systems.

🌐 Customizable OpenAI Connections: Enjoy smooth operation with custom OpenAI setups, including prefix ID support and explicit model ID support for APIs.

🔐 Ollama API Key Management: Manage Ollama credentials, including prefix ID support, for secure and efficient operation.

🔄 Connection Management: Easily enable or disable individual OpenAI and Ollama connections as needed.

🎨 Intuitive Model Workspace: Manage models across users and groups with a redesigned and user-friendly interface.

🔑 API Key Authentication: Tighten security by easily enabling or disabling API key authentication.

🔄 Unified Model Reset: Reset and remove all models from the Admin Settings with a one-click option.

🔓 Flexible Model Access Control: Easily bypass model access controls for user roles when not required, using the 'BYPASS_MODEL_ACCESS_CONTROL' environment variable, simplifying workflows in trusted environments.

🔒 Configurable API Key Authentication Restrictions: Flexibly configure endpoint restrictions for API key authentication, now off by default for a smoother setup in trusted environments.

Edit this page
Previous
API Endpoints
Next
Federated Authentication
Key Features of Open WebUI ⭐
And many more remarkable features including... ⚡️
🔧 Pipelines Support
🖥️ User Experience
💬 Conversations
💻 Model Management
👥 Collaboration
📚 History & Archive
🎙️ Audio, Voice, & Accessibility
🐍 Code Execution
🔒 Integration & Security
👑 Administration
Docs
Getting Started
FAQ
Help Improve The Docs
Community
GitHub
Discord
Reddit
𝕏
More
Release Notes
About
Report a Vulnerability / Responsible Disclosure




 🚅 LiteLLM
Hiring

Features

Pricing

Enterprise

Changelog

Docs

Github 30K

Compare features
Free
Get Started

Enterprise
Get Started

Pass-through Endpoints
Useful for migrating existing projects to the proxy. The request is passed to the provider's endpoint and the response is then passed back to the client. No translation is done.

Cost Tracking

Logging

End-user Tracking

Using LiteLLM Virtual Keys/Authentication

Logging
LLM Observability Tools (Langfuse, Langsmith, etc.)

Datadog Logging

S3 Logging

GCS Logging

Azure Data Lake

Key/Team-based Logging

Alerting/Monitoring
Slack/Discord/Teams/Email/ Webhook

Pagerduty Alerting

Prometheus Metrics

Authentication
Virtual Keys

Custom Auth

OIDC/JWT Auth

Virtual Key Rotation

Write Key to Secret Manager

CRUD Endpoints + UI
Create / Manage Users

Create / Manage Teams

Create / Manage Orgs

Assign Team Admins

Assign Org Admins

Control Model Access
Restrict Models by Key/User/Team

Model Access Groups

Team-only Models

Admin UI
Internal User Self-serve

SSO

Auto-add SSO User to Teams

Spend Tracking
Track Spend by Model/Key/User/Team

Track Spend for Org

Track Spend for Custom Tags

API endpoints for Spend Reporting

Budgets + Rate Limits
Set Budgets by Key/User/Team

Set Rate Limits by Key/User/Team

Temporary Budget Increase

Budget/Rate Limit Tiers

Guardrails
Set Guardrails per request

Default-on Guardrails

Set Guardrails by Key/Team

 🚅 LiteLLM


Product

LiteLLM Python SDK

LiteLLM Gateway (Proxy)

Docs

Getting Started - LiteLLM Gateway

Supported LLM Providers

Logging - Langfuse, OpenTelemetry etc

Prometheus Metrics

Virtual Keys

Company

Schedule call with Founders

Legal/Security/Compliance FAQ

Why Enterprise?

Careers

Resources

Slack/Discord

Docs

Get latest updates here




All Features of AnythingLLM
Click the below cards to know more about the features

AI Agents
→
API Access & Keys
→
Appearance Customization
→
Chat Logs
→
Chat Modes
→
Embedded Chat Widgets
→
Event Logs
→
Large Language Models
→
Embedding Models
→
Transcription Models
→
Vector Databases
→
Security & Access
→
Privacy & Data Handling
→
Cloud Deployment
→
System Prompt Variables
→
Last updated on September 18, 2025
Introduction




🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

Edit this page
Scroll to top
Feature Overview
AI Agents
AnythingLLM AI Agents
AI Agents
Agents are basically an LLM that has access to some simple tools. We will be adding much more customization in this area soon. All agents share the same tools across workspaces, but operate within the workspace they were invoked via @agent.

You can start an agent session by going into any workspace and typing @agent <your prompt> and exit by just typing exit

Agents can scrape websites, list and summarize your documents, search the web, make charts, and even save files to desktop and their own memory.

Examples:
1: @agent what documents can you see - > LLM will "look" at what are the documents it can see

2: @agent summarize readme.pdf - > LLM will summarize that specific embedded file

AnythingLLM AI Agents
View all the available @agent skills →
Last updated on September 18, 2025
All Features
Private Browser Tool
MIT 2025 © Mintplex Labs.
AI Agents ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Key Features
Using the Authenticated Scraping Tool
Accessing the Tool
Authentication Process
Managing Browser Data
Common Use Cases
Troubleshooting
Edit this page
Scroll to top
Feature Overview
Private Browser Tool
Desktop Only Feature (v1.8.3+)
The Authenticated Scraping tool is exclusively available in the AnythingLLM Desktop application!

Authenticated Scraping
Security Note All credentials and session data are stored locally on your machine. AnythingLLM never transmits or stores your login information outside of your local machine.

The Authenticated Scraping tool enables you to access and scrape gated online content from websites or services that require authentication but hold critical contexual content you might want to use in your workflows, such as your personal LinkedIn feed or internal company portals that you have access to.

Your LLM can now access these websites and scrape and view content just like you would in a regular browser!


Key Features
Secure Session Storage: Credentials are stored locally using isolated browser sessions
Session Persistence: Login sessions persist between app restarts until explicitly cleared or the authentication expires for the associated service
Isolated Environment: Separate from your actual web browser
Full User Control: Clear stored data or sessions at any time with a single click
Using the Authenticated Scraping Tool
Accessing the Tool
Open AnythingLLM Desktop
Navigate to Settings > Tools > Browser Tool
Click "Open Private Browser" to launch the isolated browser window

Authentication Process
Log into your desired service (e.g., LinkedIn, Gmail) through the Authenticated Scraping tool.
Your session will persist until you explicitly clear the browser data or the authentication expires for the associated service.
AnythingLLM can now access authenticated content from these services when scraping or via agentic workflow execution.
The returned content will be text only. No images, videos, or other media will be returned.
Heads up! The Authenticated Scraping tool is not a magic bullet. It is a tool that allows you to access authenticated content from websites that require authentication. It cannot currently interact with the content of the page you are accessing (eg: browser automation, RPA, etc).

Managing Browser Data
Clearing Data: Use the "Clear Browser Data" button to remove all stored credentials and sessions
When should you clear the browser data?:
When switching between different service accounts
If you encounter authentication issues when the LLM tries to access the site you want to scrape
Common Use Cases
Warning! Some web services may detect and restrict automated access, even though this tool functions as a standard browser. Use this feature responsibly and at your own discretion, as certain services may suspend or block accounts that they perceive as engaging in automated activity.

Scraping your personal linkedin profile or feed.
Accessing internal company documentation that is behind a login or SSO portal.
Collecting or accessing data from paid or authenticated web service you have access to normally.
Troubleshooting
If you encounter issues:

Clear the browser data and try again
Ensure you're fully logged into the service by opening the private browser and navigating to the site you want the LLM to access.
Some services have very short lived sessions, those services may require you to log in again after a certain amount of time or might be a bad use-case for this tool. You can always re-authenticate with the service by opening the private browser and navigating to the site you want the LLM to access and logging in again to refresh the session.

Last updated on October 31, 2025
AI Agents
API Access
MIT 2025 © Mintplex Labs.
Authenticated Scraping ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

Edit this page
Scroll to top
Feature Overview
API Access
AnythingLLM
API Access & Keys
You can find the API documentation for available endpoints on your instance at /api/docs

API keys are managed by accounts with the correct access level.

However, anyone with the API key can use the AnythingLLM API, so do not share or publish this key anywhere.

AnythingLLM supports a full developer API that you can use to manage, update, embed, and even chat with your workspaces.

You can create and delete API keys on the fly if you are allowed permission to do so.

AnythingLLM
Last updated on September 18, 2025
Private Browser Tool
Appearance Customization
MIT 2025 © Mintplex Labs.
API Access & Keys ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Custom Logo
Custom Welcome Messages
Custom Footer Links and Icons
Edit this page
Scroll to top
Feature Overview
Appearance Customization
AnythingLLM Appearance Customization
Appearance Customization
DOCKER VERSION ONLY!

These settings are only available in the Docker version of AnythingLLM

AnythingLLM allows you to customize the look and feel of your instance to match your brand and identity.

Appearance Settings Page
Overview of all the appearance settings available in AnythingLLM.

Custom Logo
Custom Logo
You can replace the AnythingLLM branded logo that appears on the login page and throughout the app with your own brand's logo. In this example, we have used a green square image for demonstration purposes.

Custom Welcome Messages
Custom Welcome Messages
By default, when you first log in to AnythingLLM and you have not yet selected a workspace, you will be shown the default messages explaining AnythingLLM. Using the system messages inputs, you can simulate both system and user response messages. Take this opportunity to tell users what specific workspaces are for - or just say hello!

Custom Footer Links and Icons
Custom Footer Links and Icons
The footer icons can be replaced with custom links and icons to provide quick access to relevant resources or web pages.

Last updated on September 18, 2025
API Access
Chat Logs
MIT 2025 © Mintplex Labs.
Appearance Customization ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

Edit this page
Scroll to top
Feature Overview
Chat Logs
AnythingLLM Workspace Chat Logs
Workspace Chat Logs
AnythingLLM supports exporting chats as:

CSV
JSON
JSON (Alpaca)
JSONL (OpenAI fine-tune)
Just click export at the top of the screen once at least 10 chat logs are available! Provided you have the correct account permissions, you can view the chat logs per workspace and per user of your AnythingLLM instance.

AnythingLLM Workspace Chat Logs
Last updated on September 18, 2025
Appearance Customization
Chat Modes
MIT 2025 © Mintplex Labs.
Workspace Chat Logs ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Query Mode vs Chat Mode
Common Questions
"It keeps saying 'No relevant information found' in Query mode"
"When should I use Query mode vs Chat mode?"
"Why does it work better with some documents than others?"
Tips for Better Results
Edit this page
Scroll to top
Feature Overview
Chat Modes
Chat Modes in AnythingLLM
AnythingLLM offers two ways to chat with your documents: Query mode and Chat mode. Let's understand what each does and how to get the best results.

Query Mode vs Chat Mode
Query Mode:

Only uses information from your uploaded documents
Will tell you if it can't find relevant information
Best for when you need accurate, document-based answers
Chat Mode:

Uses both your documents and the AI's general knowledge
More conversational and flexible
Good for brainstorming and exploring topics
Common Questions
"It keeps saying 'No relevant information found' in Query mode"
This usually means one of three things:

The information might be in your document but worded differently
The similarity settings might be too strict
The document might be too large and split in a way that makes finding information difficult
Quick fixes to try:

Go to workspace settings → Vector Database Settings
Change "Document similarity threshold" to "No restriction"
Try asking your question using words that match how it's written in your document
Instead of asking "How do I start the app?", try using terms from your document like "How do I initialize the application?"

"When should I use Query mode vs Chat mode?"
Use Query mode when:

You need factual answers from your documents
You're working with technical documentation
You want to prevent made-up information
Use Chat mode when:

You want more conversational responses
You need additional context or examples
You're brainstorming ideas
"Why does it work better with some documents than others?"
Documents are processed in chunks, and each chunk is analyzed separately. This means:

Large documents might need more specific questions
Technical documents work better with technical questions
Tips for Better Results
Start with Query mode and "No restriction" similarity if you're not finding information
Use specific terms from your documents in your questions
Switch to Chat mode if you need more context or explanation
Try rephrasing your question if you're not getting good results
If you're still not getting good results, check your workspace settings and try adjusting the "Document similarity threshold" between No restriction, Low (≥ .25), Medium (≥ .50), or High (≥ .75) to find what works best for your documents.

Last updated on September 18, 2025
Chat Logs
Embedded Chat Widgets
MIT 2025 © Mintplex Labs.
Chat Modes ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Configuration Options
Workspace
Allowed Chat Method
Restrict Requests from Domains
Max Chats per Day
Max Chats per Session
Enable Dynamic Model Use
Enable Dynamic LLM Temperature
Enable Prompt Override
Embedding the Chat Widget
Edit this page
Scroll to top
Feature Overview
Embedded Chat Widgets
AnythingLLM Embedded Chat Widgets
Embedded Chat Widgets
DOCKER VERSION ONLY!

These settings are only available in the Docker version of AnythingLLM

Embedded Chat Widget
AnythingLLM allows you to create embedded chat widgets that can be easily integrated into any website using a simple <script> tag. These embedded chat widgets provide a convenient way for users to interact with your chatbot directly from your website.

Configuration Options
When creating an embedded chat widget, you have several configuration options available to customize its behavior and appearance.

Embedded Chat Options 1
Workspace
The workspace setting determines which workspace your chat window will be based on. All defaults will be inherited from the selected workspace unless overridden by the specific configuration options.

Allowed Chat Method
You can set how your chatbot should operate using the allowed chat method. There are two options:

Chat: The chatbot will respond to all questions regardless of context.
Query: The chatbot will only respond to chats related to documents in the workspace.
Restrict Requests from Domains
This filter allows you to block any requests that come from domains other than the specified list. Leaving this field empty means anyone can use your embedded chat widget on any site.

Embedded Chat Options 2
Max Chats per Day
You can limit the number of chats this embedded chat widget can process in a 24-hour period. Setting this value to zero means unlimited chats per day.

Max Chats per Session
You can limit the number of chats a session user can send with this embedded chat widget in a 24-hour period. Setting this value to zero means unlimited chats per session.

Enable Dynamic Model Use
By enabling dynamic model use, you allow the setting of the preferred LLM model to override the workspace default.

Enable Dynamic LLM Temperature
Enabling dynamic LLM temperature allows the setting of the LLM temperature to override the workspace default.

Enable Prompt Override
By enabling prompt override, you allow the setting of the system prompt to override the workspace default.

Embedding the Chat Widget
Embedded Chat Code
After creating an embedded chat widget, you will be provided with a link that you can publish on your website using a simple <script> tag. This allows you to easily integrate the chat widget into your website's HTML code.

Last updated on September 18, 2025
Chat Modes
Event Logs
MIT 2025 © Mintplex Labs.
Embedded Chat Widgets ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Event Types
Event Details
Edit this page
Scroll to top
Feature Overview
Event Logs
AnythingLLM Event Logs
Event Logs
The Event Logs page in AnythingLLM allows users to view and monitor various events that occur within the application.

AnythingLLM Event Logs
This feature provides insights into user activities and system-related events.

Event Types
The Event Logs page captures a variety of events, such as:

User login attempts (successful and failed)
Messages sent by users
Changes made to application settings
Document uploads
Event Details
Each event in the Event Logs page includes relevant information, such as the event type, associated user (if applicable), timestamp, and any additional details specific to the event type.

Useful for monitoring your AnythingLLM instance.

Last updated on September 18, 2025
Embedded Chat Widgets
Embedding Models
MIT 2025 © Mintplex Labs.
Event Logs ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Supported Embedding Model Providers
Local Embedding Model Providers
Cloud Embedding Model Providers
Edit this page
Scroll to top
Feature Overview
Embedding Models
AnythingLLM Embedding Models
Embedding Models
AnythingLLM supports many embedding model providers out of the box with very little, if any setup.

Embedding models are specific types of models that turn text into vectors, which can be stored and searched in a vector database - which is the foundation of RAG.

Supported Embedding Model Providers
Local Embedding Model Providers
Built-in (default)
→
Ollama
→
LM Studio
→
Local AI
→
Cloud Embedding Model Providers
OpenAI
→
Azure OpenAI
→
Cohere
→
Last updated on September 18, 2025
Event Logs
Language Models
MIT 2025 © Mintplex Labs.
Embedding Models ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Supported Language Model Providers
Local Language Model Providers
Cloud Language Model Providers
Edit this page
Scroll to top
Feature Overview
Language Models
AnythingLLM Large Language Models
Large Language Models
Tip: Models that are multi-modal (text-to-text & image-to-text) are supported for System & Workspace models.

AnythingLLM allows you to use a host of LLM providers for chatting and generative AI.

Depending on your selection additional configuration might be required.

Supported Language Model Providers
Local Language Model Providers
Built-in (default)
→
Ollama
→
LM Studio
→
Local AI
→
Cloud Language Model Providers
OpenAI
→
Azure OpenAI
→
AWS Bedrock
→
Anthropic
→
Cohere
→
Google Gemini Pro
→
Hugging Face
→
Together AI
→
OpenRouter
→
Perplexity AI
→
Mistral API
→
Groq
→
KobaldCPP
→
OpenAI (generic)
→
Last updated on September 18, 2025
Embedding Models
Transcription Models
MIT 2025 © Mintplex Labs.
Large Language Models ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Supported Transcription Model Providers
Local Transcription Model Providers
Cloud Transcription Model Providers
Edit this page
Scroll to top
Feature Overview
Transcription Models
AnythingLLM Transcription Models
Transcription Models
AnythingLLM supports custom audio transcription providers.

Supported Transcription Model Providers
Local Transcription Model Providers
Built-in (Xenova)
→
Cloud Transcription Model Providers
OpenAI
→
Last updated on September 18, 2025
Language Models
Vector Database
MIT 2025 © Mintplex Labs.
Transcription Models ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Supported Vector Databases
Local Vector Databases Providers
Cloud Vector Databases Providers
Edit this page
Scroll to top
Feature Overview
Vector Database
AnythingLLM Vector Databases
Vector Databases
AnythingLLM comes with a private built-in vector database powered by LanceDB. Your vectors never leave AnythingLLM when using the default option.

AnythingLLM supports many vector databases providers out of the box.

Supported Vector Databases
Local Vector Databases Providers
LanceDB (Built-in)
→
PGVector
→
Chroma
→
Milvus
→
Cloud Vector Databases Providers
Pinecone
→
Zilliz
→
AstraDB
→
QDrant
→
Weaviate
→
Last updated on September 18, 2025
Transcription Models
Security & Access
MIT 2025 © Mintplex Labs.
Vector Databases ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Single-user Mode
Password Protecting the Instance
Multi-user Mode
User Roles
Enabling Multi-user Mode
Edit this page
Scroll to top
Feature Overview
Security & Access
AnythingLLM Security and Access
Security and Access
DOCKER VERSION ONLY!

These settings are only available in the Docker version of AnythingLLM

AnythingLLM supports two types of use cases: single-user and multi-user mode.

Single-user Mode
Single-user mode is preferred for those who only themselves or a select group of trusted people will use the instance. If you want to have per-user permissions, you should switch to multi-user mode.

In single-user mode, you (and only you) have complete control over the instance. Anyone with the password to the instance, if set, will be able to use the instance, change any configuration or settings, and view all chats.

Password Protecting the Instance
When using AnythingLLM in "single user mode," you can password protect the instance by toggling on the "Password Protect Instance" option. This will display an input where you can enter the password to protect the instance.

Password Protect Instance
You can turn off password protection at any time or reset the password to the instance while logged in.

Multi-user Mode
Warning

Once in multi-user mode, you cannot revert back to single-user mode

The preferred method of use for AnythingLLM is multi-user mode. In this mode, you can set per-user role-based access permissions.

By default, you will create the administrator account, which has the highest level of privilege. As an administrator, you will have access to the entire system, logs, analytics, and more.

User Roles
Admin: Full access to the entire system
Manager: Can view all workspaces and manage all properties except for settings for LLM, Embedder, and Vector database
Default: Can only send chats to workspaces they are explicitly added to. Cannot see or edit any workspaces or system settings.
Enabling Multi-user Mode
To enable multi-user mode, toggle on the "Enable multi-user mode" option. This will display an input where you can enter the username and password for the first admin account.

Enable Multi-user Mode
This will be the default admin account that you will use to control the instance. Once set, you will be logged out so you can log in with the new password.

Last updated on September 18, 2025
Vector Database
Privacy & Data Handling
MIT 2025 © Mintplex Labs.
Security and Access ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Anonymous Telemetry
Edit this page
Scroll to top
Feature Overview
Privacy & Data Handling
AnythingLLM Privacy & Data
Privacy & Data Handling
Tip:

AnythingLLM is transparent telling you who and what has access to your data.

Privacy & Data
Anonymous Telemetry
AnythingLLM collects anonymous telemetry and never collects any of your personal data.

We collect telemetry to help improve our product.

If for any reason you would not like to participate in sharing telemetry with us, you can disable it in this menu.

Last updated on September 18, 2025
Security & Access
System Prompt Variables
MIT 2025 © Mintplex Labs.
Privacy & Data ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
All Features
AI Agents
Private Browser Tool
API Access
Appearance Customization
Chat Logs
Chat Modes
Embedded Chat Widgets
Event Logs
Embedding Models
Language Models
Transcription Models
Vector Database
Security & Access
Privacy & Data Handling
System Prompt Variables
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Default Variables
Custom Variables
How to use system prompt variables
UI Example:
Edit this page
Scroll to top
Feature Overview
System Prompt Variables
System Prompt Variables
System prompt variables allow you to inject dynamic and static variables into your system prompt on the fly. This is useful for a variety of use cases, such as:

Injecting the user's name into the system prompt
Injecting the current date and time into the system prompt
Injecting static information into the system prompt like your company's name
and more!
Default Variables
AnythingLLM can have varying default variables depending on if you are using the AnythingLLM via Docker or AnythingLLM Desktop version.

AnythingLLM comes with a set of default variables that you can use in your system prompt. You can view the full list of active variables by clicking on the System Prompt Variables link in the sidebar under Tools when on the settings page.

AnythingLLM System Prompt Variables
Variable	Description	Available in
{date}	The current date	ALL VERSIONS
{time}	The current time	ALL VERSIONS
{datetime}	The current date and time	ALL VERSIONS
{user.name}	The name of the user	AnythingLLM Docker (with multi-user mode enabled)
{user.bio}	The bio field of the user	AnythingLLM Docker (with multi-user mode enabled)
{os.name}	The name of the operating system	AnythingLLM Desktop
{os.arch}	The architecture of the operating system	AnythingLLM Desktop
Note: Any time based variable will the current time of the machine AnythingLLM is running on. Keep this in mind in Docker based versions of AnythingLLM.

Custom Variables
You can also create your own custom variables by clicking the Add Variable button on the System Prompt Variables page.

AnythingLLM Custom Variables
All user created variables are static values and will not change when expanded into a system prompt.

How to use system prompt variables
Invalid variables will simply not be expanded into the system prompt - you will not see an error message during an LLM request.

You can tell if a variable is invalid once you stop editing the system prompt and it is not highlighted in blue in the UI.

System prompt variables can be used any workspace's System Prompt field. You can inject a variable by editing the system prompt and using the variable in the prompt.

Example:

You are a helpful assistant.
Today is {date} and the current time is {time}.
The user's name is {user.name}, they work at {company_name} and this is what we know about them:
{user.bio}
When expanded into a system prompt, it will look like this:

You are a helpful assistant.
Today is 2024-01-01 and the current time is 12:00:00.
The user's name is John Doe, they work at Google and this is what we know about them:
Rock climbing is my favorite hobby and I am obsessed with optimizing AI agents and workflows.
UI Example:
AnythingLLM System Prompt Variables
Last updated on September 18, 2025
Privacy & Data Handling
Overview
MIT 2025 © Mintplex Labs.
System Prompt Variables ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

User messages
Actions
LLM messages
Actions
Prompt Input Controls
Edit this page
Scroll to top
Chat Interface overview
AnythingLLM Chat UI
Overview of the chat interface
The chat interface of AnythingLLM is where you will spend most of your time when using AnythingLLM, as such you should familiarize yourself with the basics. This page could have some additional icons that are not in the above image, as we are always improving AnythingLLM.

The above image may seem like a lot, but you will soon find the interface intuitive and familiar with other interfaces you have used.

User messages
User messages are messages that you have sent. This is the text that is used to find similar documents as well as what is sent to the LLM.

Actions
Copy: Copy the content of this text box.
Edit: Editing a message allows you to amend and automatically resubmit the conversation from that point to the LLM. Beware that this will truncate all messages below the edited content.
Speak: Use the operating system native text-to-speech module, OpenAI Voice, or an 11Labs voice to speak your text.
LLM messages
LLM messages are responses from your LLM that are active in this chat session. This is the text that is used to find similar documents as well as what is sent in future conversations. History is automatically managed when the context window is exceeded.

Actions
Copy: Copy the content of this text box.
Edit: Editing a message allows you to amend the output of an LLM message for correctness. This does not resubmit your prompt and simply will update the history.
Regenerate: Resend a prompt back to the LLM with the same prompt and history to get a new answer.
Feedback (Thumbs Up & Thumbs Down): Allow the user to leave qualitative feedback on an LLM response. Leaving feedback has no impact on message history or future responses. Feedback metrics are most useful for exporting of chats to be able to sort through good responses for creating fine-tunes outside of AnythingLLM.
Prompt Input Controls
Slash Commands: Slash Commands are ways to inject some standard text into your prompt where that command is present. It is basically a short-key for text snippets. You can create and manager your slash commands here.
Default Slash Commands: These are special commands built by the core-team that have special functions like /reset
@agent Invocation: View all available @agents and their available skill sets. Using @agent at the start of a prompt will start an agent session. Learn more about agents here.
Font Size: Set the default font size for your profile of AnythingLLM.
Microphone: Enable voice-to-text inputs for your LLM prompts.This feature is not available on Desktop.
Last updated on September 18, 2025
Zilliz
Other configurations
MIT 2025 © Mintplex Labs.
ChatUI Walkthrough ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
What is NVIDIA NIM?
System Requirements
Installation Walkthrough
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Privacy
How does it work?
What models are supported?
How do I install it?
Definitions
Video Walkthrough & Overview
Edit this page
Scroll to top
NVIDIA NIM Integration
What is NVIDIA NIM?
NVIDIA NIM is being phased out of AnythingLLM Desktop and will be removed in a future version.

As an alternative, we recommend using Microsoft Foundry Local which is a free and open source LLM engine that runs on your local machine.

You are also welcome to use any other local LLM engine like Ollama or LM Studio or our internal built in LLM engine that comes with AnythingLLM Desktop.

What is NVIDIA NIM?
NVIDIA NIM (aka: Nvidia Inference Microservices) is a software technology, which packages optimized inference engines, industry-standard APIs and support for AI models into containers for easy deployment.

All of this runs via WSL2 on Windows and makes it easy to deploy and run LLM models locally at the fastest speeds possible on RTX AI PC's. AnythingLLM features a bespoke integration in the AnythingLLM Desktop client that makese installation, setup, and usage of NIM a breeze.

NVIDIA NIM is currently in beta and is only available on Windows 11 on AnythingLLM Desktop.

Privacy
NVIDIA NIM models run fully locally on your machine using your own GPU. AnythingLLM does not send any data to NVIDIA or any other third party in order to run NIM models. After a model is installed, it is present on your local machine and AnythingLLM will use this local engine for inference.

NVIDIA NIM on RTX is not to be confused with NVIDIA's cloud-based NIM offering. This is a completely separate product and service designed to run NIM on your local RTX GPU.

How does it work?
A NIM is a single model + software stack, packaged into a container designed and maintained by NVIDIA. It is specificially designed to be run on NVIDIA RTX GPUs. In AnythingLLM, we use NIM to run the LLM models for chat, agents, and all other tasks that require inference.

See the NVIDIA NIM system requirements for the full list of requirements to run NIM models on your system.

What models are supported?
AnythingLLM supports all of the models that are available in the NIM containers. You can see the full list of models on build.nvidia.com.

How do I install it?
AnythingLLM will present you with a simple to use UI to install and manage NIM containers if you select the NVIDIA NIM LLM provider and are on a compatible operating system.

Once the official NIM installer has finished, you will be able to use NVIDIA NIM models in AnythingLLM.

See the NVIDIA NIM x AnythingLLM Walkthrough for the full walkthrough.

Definitions
NIM: Nvidia Inference Microservice - a single LLM or Model + software stack, packaged into a container designed and maintained by NVIDIA.
WSL2: Windows Subsystem for Linux 2 - a compatibility layer that allows you to run Linux binaries on Windows 11. You will not need to directly interact with WSL2 - the NIM installer will handle this for you and AnythingLLM will use it automatically.
NIM Installer: The pre-built NVIDIA NIM installer that runs in the AnythingLLM Desktop client to unlock the use of NIM models in AnythingLLM.
NIM Manager: The AnythingLLM UI that allows you to install, update, and run a NIM.
Video Walkthrough & Overview

Last updated on October 9, 2025
Install the AnythingLLM Browser Extension
System Requirements
MIT 2025 © Mintplex Labs.
What is NVIDIA NIM? ~ AnythingLLM


🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
What is NVIDIA NIM?
System Requirements
Installation Walkthrough
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

Select the NVIDIA NIM LLM Provider
Fresh install
Post install
Running the NIM Installer
Swap to Managed Mode
Installing your first model
Monitoring your model download
Starting your first NIM
Streaming logs from the NIM
How do I know when my NIM is ready to use?
Selecting your NIM in AnythingLLM
Stopping your NIM
Deleting your NIM
Edit this page
Scroll to top
NVIDIA NIM Integration
Installation Walkthrough
NVIDIA NIM is being phased out of AnythingLLM Desktop and will be removed in a future version.

As an alternative, we recommend using Microsoft Foundry Local which is a free and open source LLM engine that runs on your local machine.

You are also welcome to use any other local LLM engine like Ollama or LM Studio or our internal built in LLM engine that comes with AnythingLLM Desktop.

NVIDIA NIM Walkthrough
The use of NVIDIA NIM in AnythingLLM is very simple and straightforward - all of the complexity is hidden from you by the AnythingLLM Desktop client or the NVIDIA NIM Installer.

Select the NVIDIA NIM LLM Provider
In AnythingLLM Desktop, select the NVIDIA NIM LLM provider from the dropdown menu - this will show your the default NIM connector.

If you do not see the blue model with the button as show in the below images, your system is not compatible with running a NIM. Please see the system requirements for more information.

Fresh install
If you have never run the NVIDIA NIM installer before, you will see the following screen:


Post install
If you have already run the NVIDIA NIM installer before or otherwise have all of the NIM pre-requisites installed, you will see the following screen:


You can see the blue button has changed to "Swap to Managed Mode" and you can click on it to enable managed mode.

Running the NIM Installer
This step only needs to be run once per machine. Once NVIDIA NIM is installed, you will not need to run the installer ever again.

See Swap to Managed Mode for more information on how to use NVIDIA NIM in managed mode.

If you encounter any issues with the NIM installer you can get help from NVIDIA via: - NVIDIA NIM Community Forums - Technical Support - [NVIDIA NIM AI RTX PC Discord

General Discussion & Announcements](https://discord.gg/nvidiadeveloper)
The official NVIDIA NIM installer is a pre-built binary that runs in the AnythingLLM Desktop client built by NVIDIA. If your system or GPU is not compatible with running a NIM, you will see an error message during this step and will be unable to run a NIM on AnythingLLM or your system in general.

Clicking on the "Run NVIDIA NIM Installer" button will prompt your to run the NIM installer as a separate window.

If you want to run the NIM installer manually, you can download the installer from NVIDIA directly via their WSL2 docs.


Click through the installer and follow the instructions to install NVIDIA NIM. This process will take a few minutes to complete and may require a restart of your machine post-installation.


Swap to Managed Mode
After closing the completed NIM installer, you will see the blue button change to "Swap to Managed Mode". Clicking on this button will allow AnythingLLM to manage your NIM models for you via a simple UI.


This is the recommended mode of operation for AnythingLLM as it will allow you to easily update your NIM models and manage your NIM instances. Once you have swapped to managed mode, you will see the NIM manager UI with no models.


Installing your first model
To install your first model, click on the "Import NIM from NVIDIA" button in the NIM manager UI at the top of the screen.

Here you will see a short list of pre-selected and recommended models for you to choose from. Clicking on any of the models will begin the download process after prompting a short license agreement dialog.


You can however select any model from the NVIDIA NIM catalog and paste it's model ID into the input field and click "Pull Model" to install it - however this is not recommended.

Monitoring your model download
NIM models are more than just a single GGUF, which you may be used to from other LLM providers. NIM models are the model + software to run the model as fast as possible on your RTX GPU - so they can be a bit larger than your typical GGUF.

You can monitor the progress of the model download in the NIM manager UI by clicking on the blue text link below the the "Import NIM from NVIDIA" button. This will show you the live download progress.

The speed of the download will vary depending on your internet connection speed and the model you are downloading.

You can close this window at any time and it will not affect the download in any way.


You will see the text "Pulling image from NGC Registry Completed" when the model has finished downloading and is unpacked and ready to use.


Starting your first NIM
The very first time you start a NIM, it will take a few minutes to download additional model files start its inference service. This is normal and expected and subsequent starts will be much faster.

You can monitor the progress of the NIM starting in the NIM manager UI by clicking on the blue text link below the the "logs" button. This will show you the live startup progress.

Clicking on the "Refresh" button in the NIM manager UI will show you all of the NIMs you have installed. Models that have never been started will show a "Start NIM" button. You can click on this button to start the NIM.

This will begin the process of starting the NIM and you will see the NIM status change to "Starting NIM..." in the NIM manager UI as well as see VRAM begin to be allocated to the NIM.


Once the NIM has started, you will see the NIM status change to "NIM Started" as well as the ability to Stop and Delete the NIM and see its logs.


Streaming logs from the NIM
You can stream the logs from the NIM by clicking on the "Logs" button in the NIM manager UI. This will open a new tab with the NIM logs. You can close this window at any time and it will not affect the NIM in any way.


How do I know when my NIM is ready to use?
In the NIM logs, you will see the following message in the log output:

// a bunch of other logs
Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

This means that your NIM is ready to use! You can now start using it in AnythingLLM.

Selecting your NIM in AnythingLLM
To select your NIM in AnythingLLM, simply click on the model card for the NIM you want to use and click "Save changes" in the top right.


You can now use this model in AnythingLLM as you would any other model or provider.

Stopping your NIM
Since running a NIM will reserve VRAM on your GPU, we recommend that you stop your NIM when you are not using it. You can stop your NIM by clicking on the "Stop NIM" button in the NIM manager UI. This will begin the process of stopping the NIM and you will see the NIM status change to "Stopping NIM..." in the NIM manager UI as well as see VRAM begin to be deallocated from the NIM.

Closing AnythingLLM currently does not stop the NIM - so you will need to manually stop the NIM by clicking on the "Stop NIM" button in the NIM manager UI.

Deleting your NIM
You can delete your NIM by clicking on the "Delete NIM" button in the NIM manager UI. This will delete the NIM instance, but will not delete the model from your system. If you wish to delete the model from your system, you will need to do so manually via WSL.

wsl -d NVIDIA-Workbench
podman image ls # Will show you all of the images on your system
podman rmi <image_id> # Will delete the image from your system - the container should be deleted prior to this
This will delete the NIM image from your system totally.

Last updated on October 9, 2025
System Requirements
Attaching vs RAG
MIT 2025 © Mintplex Labs.
Walkthrough ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

What even is an agent?
Some LLMs are bad at generating JSON and even worse at following instructions.
Model is hallucinating a tool call.
Common Solutions
LLM says it cannot call XYZ tool.
Common Solutions
LLM is refusing to even detect or call a tool at all.
Common Solutions
Edit this page
Scroll to top
AI Agent not using tools!
Why is my @agent not using tools!
AI Agents unlock new and exciting ways to use and leverage LLMs to do things for you as opposed to just reply with text. However, these LLMs are still not fully intelligent and like other implementations of LLMs - this method is not without its "gotchas".

Like other LLM problems, this mostly comes down to the model you are using and as always a more powerful & capable model yields better results. When using agents, we recommend the best model you can run.

caveat: There are some smaller models that are specifically trained for JSON/function calling and they can be used in lieu of just a larger model, but this has its own drawbacks when you want to then get the final response back as a normal chat. In general, you should use a general text/instruct model.

What even is an agent?
Without getting too technical there is some foundational knowledge to understand what an "AI Agent" even is. The below graphics really describe what LLMs are doing and "reasoning" about. As you can see, its no different that a specifically formatted text response!


So now that we know LLMs are basically doing an extra step in between your prompt and it's final answer, any agent's implementation usually goes wrong in the JSON generation part.

Okay, so now that we know how this pipeline works in order for an agent to even function works, how can we solve and debug issues?

Some LLMs are bad at generating JSON and even worse at following instructions.
Tip: Cloud based (un-quantized) models are typically dramatically better at following instructions and forming valid JSON matching the required tool-call.

You can use a cloud based model for just agent calls in AnythingLLM and use an open-source model for normal chatting.

The main issue we see with agents are people who want to use a smaller parameter model that is heavily quantized and want to get GPT-level quality tool interactions. Below are the reasons + ways to mitigate the effects of bad tool calls and their common solutions.

Model is hallucinating a tool call.
When a tool is actually called you will see what we call a "thought" output to the UI. This indicates that the tool was actually called. If the LLM responds with information and you don't see a thought-chain, it is likely making up the output and pretended to call a tool.


Common Solutions
Swap to a high quantization version or larger param model
/reset chat history and re-ask the prompt
LLM says it cannot call XYZ tool.
Some models are aligned too heavily and will refuse to use some tools because of their training. This is common for requests like website scraping.

Common Solutions
Swap to a high quantization version, larger param model, or less restricted model
/reset chat history and re-ask the prompt
Turn off tools you are not using to reduce prompt window size
LLM is refusing to even detect or call a tool at all.
Open-source models, with their quantization and limited context window are susceptible to just refusing to discover or call a tool properly.

When tools are injected into the LLMs prompt for discovery and execution they can quite often be "overloaded" with information or due to their quantization are unable to create valid JSON that exactly matches the schema required for a tool call to succeed. The LLM is simply generating JSON, something lower-param and quantized models are particularly bad at!

AnythingLLM however does make some significant corrections to have slightly invalid JSON be formatted properly so a call can succeed, but we can only do so much on this front.

Common Solutions
Swap to a high quantization version, larger param model, or less restricted model
/reset chat history and re-ask the prompt (chat history can sometimes impact output of JSON)
Turn off tools you are not using to reduce prompt window size and load on prompt.
Last updated on September 18, 2025
RAG in AnythingLLM
Ollama Connection Debugging
MIT 2025 © Mintplex Labs.
Why is my AI Agent not using tools! ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

General Troubleshooting (Desktop & Docker)
Ensure Ollama server is Running
Troubleshooting (Docker)
localhost and 127.0.0.1 do not work on Docker.
Troubleshooting (Remote Ollama)
AnythingLLM Cloud + Local Ollama
Edit this page
Scroll to top
Ollama Connection Debugging
Connecting to Ollama is a very simple process, but sometimes things can appear to not being working depending on if you are using the AnythingLLM Desktop version or running AnythingLLM via Docker.

In general, all AnythingLLM instances just need a valid URL to connect to Ollama running anywhere, however there can be some nuances depending on how you are running AnythingLLM or Ollama - in any case, all that is needed is a reachable URL to connect to Ollama.

The most common issue people run into is trying to use localhost or 127.0.0.1 to connect to Ollama running on their local machine when running AnythingLLM via Docker - see the Troubleshooting (Docker) section for how to fix this.

General Troubleshooting (Desktop & Docker)
On both the Desktop and Docker versions of AnythingLLM, the Ollama URL is automatically detected if we can detect it. If the Ollama URL is not detected, you will need to manually set the Ollama URL in the AnythingLLM settings.

The list of automatically detected URLs is as follows:

http://127.0.0.1:11434
http://host.docker.internal:11434
http://172.17.0.1:11434
If your Ollama URL is not detected because it is not in the list above, you will need to manually set the Ollama URL in the AnythingLLM settings - which will be shown in the UI for you to modify.

Ensure Ollama server is Running
Before attempting any fixes or URL changes, verify that Ollama is running properly on your device:

Open your web browser and navigate to http://127.0.0.1:11434
You should see a page similar to this:
Ollama running in background
If you don't see this page, troubleshoot your Ollama installation and ensure that it is running properly before moving forward as well as make sure you run the ollama serve command. Most of the time, Ollama will automatically start the server when ollama is running.

Running ollama run model-name will not start the server - this is only for running models in your command line and you will not be able to use the Ollama API with this command.

Troubleshooting (Docker)
If you are running AnythingLLM via Docker and you are trying to connect to Ollama running locally on your machine.

If you are seeing no models loaded in AnythingLLM or getting error responses from Ollama - 100% of the time this is beacause you are using the wrong URL in the connection in AnythingLLM.

localhost and 127.0.0.1 do not work on Docker.
On Docker, localhost and 127.0.0.1 are not valid URLs for the Docker container Ollama connection in AnythingLLM because both of these refer to the container network and not the host machine.

To fix this, you can use the host.docker.internal (Windows/MacOS) or 172.17.0.1 (Linux) URLs to connect to the host machine from the Docker container with the same port (default 11434).

Running Docker on Windows or MacOS (available since Docker version 18.03):

http://localhost:11434 => http://host.docker.internal:11434
http://127.0.0.1:11434 => http://host.docker.internal:11434
Running Docker on Linux:

http://localhost:11434 => http://172.17.0.1:11434
http://127.0.0.1:11434 => http://172.17.0.1:11434
Troubleshooting (Remote Ollama)
If you are running AnythingLLM via Docker and are trying to connect to Ollama running on another machine the underlying principle is the same where the Ollama URL is the IP address of the machine running Ollama.

In the case of a remote Ollama, the Ollama URL is the IP address of the machine running Ollama and it is your responsibility to ensure that the IP address is correct, your firewall rules are correct, and that the machine is running ollama. There is no way for AnythingLLM to automatically detect the IP address of the machine running Ollama.

AnythingLLM Cloud + Local Ollama
You cannot connect to Ollama running on your local machine when using AnythingLLM Cloud. This would require you to expose your local machine to the internet long-term via a service like ngrok which is not recommended and not secure.

While it is possible, we do not recommend it and it is your discretion to do so if you understand the security implications of SSH tunneling your local machine to the internet. We will not provide support for any issues related to exposing your local machine to the internet.

Last updated on September 18, 2025
AI Agent not using tools!
Fetch failed error on embed
MIT 2025 © Mintplex Labs.
General Help ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

What is this?
Check if the machine running AnythingLLM is blocking downloads from HuggingFace or AWS.
Why is this happening?
How to fix it?
Windows Visual C++ Redistributable
Why is this happening?
How to fix it?
Your CPU is not supported
Why is this happening?
How to fix it?
Edit this page
Scroll to top
Fetch failed error on embed
What is this?
When you try to embed a file in AnythingLLM, you might see a "Fetch failed" error. There are a few reasons why this might happen and all of them are fixable quite easily and are all related to the machine running AnythingLLM or firewall permissions.

Below are the most common fixes for this error ordered from the most likely to the least likely.

Check if the machine running AnythingLLM is blocking downloads from HuggingFace or AWS.
This error applies to you if:

 You are using the default AnythingLLM embedder model
 You may have a firewall blocking downloads from HuggingFace or AWS either by default or because you have a custom firewall installed by whoever manages your network.
Why is this happening?
This error happens when the machine running AnythingLLM is blocking downloads from HuggingFace or AWS. We do not pre-bundle the embedding model into the app, so the machine needs to download the model for its very first use. After it is downloaded, the model is cached so it doesn't need to be downloaded again. Your embeddings for the default embedder model are always done locally, this is just a problem with downloading the model GGUF and tokenizer.

How to fix it?
Check your storage folder and see if a folder named models/Xenova exists.
If this folder does not exist, it's likely that the machine is blocking downloads from HuggingFace or AWS.
Unblock the huggingface.co and api.huggingface.co domains on your machine.
Try embedding again.
Unblock this origin: https://cdn.anythingllm.com/support/models/
Try embedding again.
Still not working? Try the next solution.

Windows Visual C++ Redistributable
This error applies to you if:

 You are using the default AnythingLLM embedder model
 You are on Windows
Why is this happening?
This error happens when the machine running AnythingLLM is missing the Windows Visual C++ Redistributable. This is a library that is required to run the model.

How to fix it?
Download the Visual C++ Redistributable v14.x and install it.
Try embedding again.
Still not working? Try the next solution.

Your CPU is not supported
This error applies to you if:

 You are using the default AnythingLLM vector database
Why is this happening?
LanceDB is a vector database that is used to store the embeddings. It is the default vector database for AnythingLLM.

Your CPU is not supported if you are using a CPU that does not support AVX2.

How to fix it?
Use a machine with a supported CPU.
Use another vector database provider for vector storage. We support most of the popular vector databases.
Last updated on September 18, 2025
Ollama Connection Debugging
Manual QNN Model Download
MIT 2025 © Mintplex Labs.
'Fetch failed' error on embed ~ AnythingLLM

🚀 AnythingLLM v1.9.1 is live! Update now →

AnythingLLM Docs
Mintplex Labs
Search documentation…
Discord
▲ Home
AnythingLLM Roadmap
Getting Started
Introduction
Feature Overview
AnythingLLM Setup
Chat Interface overview
Other configurations
AnythingLLM Community Hub
What is the Community Hub?
Importing an item
Uploading an item
FAQ
Installation Guides
AnythingLLM Desktop
AnythingLLM Self-hosted
AnythingLLM Cloud
AnythingLLM Mobile
Guides
MCP Compatibility
Agent Flows
Using AI Agents
Importing custom models
AnythingLLM Browser Extension
NVIDIA NIM Integration
Frequently Asked Questions
Using Documents in Chat
AI Agent not using tools!
Ollama Connection Debugging
Fetch failed error on embed
Manual QNN Model Download
More
Beta Previews
Desktop Changelogs
Contribute
Community Hub
Support

System

On This Page

What is this?
Download the models
Once your zip file is downloaded
Edit this page
Scroll to top
Manual QNN Model Download
What is this?
Sometimes you need to download the NPU models manually due to connection issues. This is a manual process but it's quite simple to do and should only be done if you are unable to download the models automatically from selecting them in the GUI on the desktop app.

Download the models
You can download the models from the following links:

Llama-3.2-3B-Chat (8k context)
Llama-3.2-3B-Chat (16k context)
Llama-3.1-8B-Chat (8k context)
Phi 3.5-mini-instruct (4k context)
Once your zip file is downloaded
Open the models/QNN folder (or create it if it doesn't exist) in the desktop storage folder.
Move the zip file into this folder.
Extract the zip file.
You should now have a folder named with the same name as the zip file and inside it will be the model files.

# Example folder structure
models/QNN/
└── llama_v3_2_3b_chat_8k/
    ├── genie_config.json
    ├── htp_backend_etc.bin
    ├── related-model-bin-file.bin
    └── tokenizer.json
Restart the desktop app. Now the model should be available in the GUI to be selected and used for inference.
Last updated on September 18, 2025
Fetch failed error on embed
What are beta previews?
MIT 2025 © Mintplex Labs.
Manual QNN Model Download ~ AnythingLLM

