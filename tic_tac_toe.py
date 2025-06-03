import streamlit as st
import time

st.set_page_config(page_title="Tic-Tac-Toe", page_icon="❌", layout="centered")
st.markdown("<h1 style='text-align: center;'>❌ Tic-Tac-Toe ⭕</h1>", unsafe_allow_html=True)
st.markdown("---")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# Check for winner
def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Render a single row with vertical lines
def render_row(row_idx):
    cols = st.columns([1, 0.05, 1, 0.05, 1])  # 3 game cells and 2 lines
    for i in range(3):
        cell_index = row_idx * 3 + i
        if st.session_state.board[cell_index] == "":
            if cols[i * 2].button(" ", key=cell_index, use_container_width=True):
                st.session_state.board[cell_index] = st.session_state.turn
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
        else:
            cols[i * 2].markdown(
                f"<h2 style='text-align: center;'>{st.session_state.board[cell_index]}</h2>",
                unsafe_allow_html=True,
            )
        if i < 2:
            cols[i * 2 + 1].markdown("<div style='height: 50px; border-left: 3px solid black;'></div>", unsafe_allow_html=True)

# Display board
def render_board():
    for row in range(3):
        render_row(row)
        if row < 2:
            st.markdown("<hr style='border: 2px solid black;'>", unsafe_allow_html=True)

render_board()

# Show result
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.markdown("## 🤝 It's a Draw!")
    else:
        st.markdown(f"## 🏆 Player {st.session_state.winner} Wins!")
        st.balloons()
    
    st.markdown("### 🔁 Restarting game in 5 seconds...")
    time.sleep(5)
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None
    if st.button("Play Again"):
        st.experimental_rerun()

st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
