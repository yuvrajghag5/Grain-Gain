// Constants
const CATEGORIES = [
    { name: 'Vegetables', icon: '🥬' },
    { name: 'Fruits', icon: '🍎' },
    { name: 'Lentils', icon: '🫘' },
    { name: 'Dairy', icon: '🥛' },
    { name: 'Meat', icon: '🥩' },
    { name: 'Fish', icon: '🐟' },
    { name: 'Grain', icon: '🌾' },
    { name: 'Nuts', icon: '🥜' },
    { name: 'Seeds', icon: '🌱' }
];

const CATEGORY_ITEMS = {
    'Vegetables': ['Tomato', 'Carrot', 'Spinach', 'Broccoli'],
    'Fruits': ['Apple', 'Banana', 'Orange', 'Mango'],
    'Lentils': ['Red Lentils', 'Green Lentils', 'Yellow Lentils'],
    'Dairy': ['Milk', 'Cheese', 'Yogurt', 'Butter'],
    'Meat': ['Chicken', 'Beef', 'Pork', 'Lamb'],
    'Fish': ['Salmon', 'Tuna', 'Cod', 'Sardines'],
    'Grain': ['Rice', 'Wheat', 'Oats', 'Quinoa'],
    'Nuts': ['Almonds', 'Walnuts', 'Cashews', 'Pistachios'],
    'Seeds': ['Chia', 'Flax', 'Sunflower', 'Pumpkin']
};

// State Management
let currentUser = null;
let currentScreen = 'login';

// DOM Elements
const screens = document.querySelectorAll('.screen');
const navBar = document.getElementById('navigation-bar');

// Screen Management
function showScreen(screenId) {
    screens.forEach(screen => screen.classList.remove('active'));
    document.getElementById(`${screenId}-screen`).classList.add('active');
    currentScreen = screenId;
    
    // Show/hide navigation bar
    navBar.style.display = screenId === 'login' ? 'none' : 'flex';
    
    // Update active nav item
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.toggle('active', item.dataset.screen === screenId);
    });
}

// Login Management
document.getElementById('signin-button').addEventListener('click', () => {
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    
    if (email && password) {
        currentUser = { email };
        document.getElementById('profile-email').textContent = email;
        showScreen('main');
    }
});

document.getElementById('create-account-button').addEventListener('click', () => {
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    
    if (email && password) {
        currentUser = { email };
        document.getElementById('profile-email').textContent = email;
        showScreen('main');
    }
});

// Password Toggle
document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', (e) => {
        const passwordInput = e.target.parentElement.querySelector('input');
        passwordInput.type = passwordInput.type === 'password' ? 'text' : 'password';
    });
});

// Categories Grid
function populateCategoriesGrid() {
    const grid = document.getElementById('categories-grid');
    grid.innerHTML = CATEGORIES.map(category => `
        <div class="category-item" data-category="${category.name}">
            <div class="category-icon">${category.icon}</div>
            <span>${category.name}</span>
        </div>
    `).join('');
    
    // Add click handlers
    grid.querySelectorAll('.category-item').forEach(item => {
        item.addEventListener('click', () => {
            const category = item.dataset.category;
            showCategoryPage(category);
        });
    });
}

// Category Page
function showCategoryPage(category) {
    document.getElementById('category-title').textContent = category;
    const itemsContainer = document.getElementById('category-items');
    itemsContainer.innerHTML = CATEGORY_ITEMS[category].map(item => `
        <div class="item-card">
            <span>${item}</span>
            <button class="primary-button">Add</button>
        </div>
    `).join('');
    showScreen('category');
}

// Search Functionality
function performSearch(searchText) {
    const results = [];
    for (const category in CATEGORY_ITEMS) {
        CATEGORY_ITEMS[category].forEach(item => {
            if (item.toLowerCase().includes(searchText.toLowerCase())) {
                results.push({ name: item, category });
            }
        });
    }
    return results;
}

document.getElementById('search-button').addEventListener('click', () => {
    const searchText = document.getElementById('search-page-input').value;
    const results = performSearch(searchText);
    displaySearchResults(results);
});

function displaySearchResults(results) {
    const container = document.getElementById('search-results');
    if (results.length === 0) {
        container.innerHTML = '<p class="no-results">No items found</p>';
        return;
    }
    
    container.innerHTML = results.map(item => `
        <div class="search-result-item">
            <div>
                <h3>${item.name}</h3>
                <p>Category: ${item.category}</p>
            </div>
            <button class="primary-button">Add</button>
        </div>
    `).join('');
}

// Navigation
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
        if (item.id === 'signout-button') {
            // Handle sign out
            currentUser = null;
            showScreen('login');
            return;
        }
        
        const targetScreen = item.dataset.screen;
        if (targetScreen) {
            showScreen(targetScreen);
        }
    });
});

// Camera functionality (placeholder)
document.querySelector('[data-screen="camera"]').addEventListener('click', () => {
    alert('Camera access would be implemented in a real mobile app');
});

// Main search bar functionality
document.getElementById('search-input').addEventListener('input', (e) => {
    const searchText = e.target.value;
    if (searchText) {
        const results = performSearch(searchText);
        if (results.length > 0) {
            showScreen('search');
            displaySearchResults(results);
            document.getElementById('search-page-input').value = searchText;
        }
    }
});

// Initialize app
function initializeApp() {
    // Populate categories grid
    populateCategoriesGrid();
    
    // Show initial screen
    showScreen('login');
    
    // Hide navigation bar initially
    navBar.style.display = 'none';
    
    // Add back button functionality for category pages
    document.querySelector('.back-button')?.addEventListener('click', () => {
        showScreen('main');
    });
}

// Start the application
document.addEventListener('DOMContentLoaded', initializeApp);

// Handle browser back button
window.addEventListener('popstate', () => {
    if (currentScreen !== 'login' && currentUser) {
        showScreen('main');
    }
});

// Add to cart functionality (placeholder)
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('primary-button') && 
        e.target.textContent === 'Add') {
        alert('Item added to cart!');
    }
});

// Prevent form submission refresh
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', (e) => e.preventDefault());
});
