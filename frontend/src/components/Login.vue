<template>
  <div class="login-page">
    <div class="login-container">
      <div class="logo">
        <svg width="100" height="40" viewBox="0 0 100 40">
          <path d="M10,20 C10,14.5 14.5,10 20,10 H80 C85.5,10 90,14.5 90,20 V30 C90,35.5 85.5,40 80,40 H20 C14.5,40 10,35.5 10,30 V20 Z" fill="#1a73e8"/>
          <text x="50" y="28" fill="white" text-anchor="middle" font-size="14" font-weight="bold">KYC AUTH</text>
        </svg>
      </div>
      
      <!-- Email Step -->
      <div v-if="currentStep === 'email'" class="step-container">
        <h1>Sign in</h1>
        <p class="subtitle">Continue to KYC Auth</p>
        
        <div class="form-group">
          <div class="form-control" :class="{ 'focused': isEmailFocused || email }">
            <input 
              type="email" 
              id="email" 
              v-model="email" 
              @focus="isEmailFocused = true" 
              @blur="isEmailFocused = false"
              @keyup.enter="goToPasswordStep"
              placeholder=" "
              ref="emailInput"
            >
            <label for="email">Email or phone</label>
          </div>
          <a href="#" class="forgot-link">Forgot email?</a>
        </div>
        
        <!-- <p class="subtitle privacy-notice">Not your computer? Use Guest mode to sign in privately.</p> -->
        
        <div class="bottom-container">
          <a href="/registeruser" class="create-account">Create account</a>
          <button class="next-btn" @click="goToPasswordStep" @mouseover="isNextHovered = true" @mouseleave="isNextHovered = false" :class="{ 'hovered': isNextHovered }">Next</button>
        </div>
      </div>
      
      <!-- Password Step -->
      <div v-if="currentStep === 'password'" class="step-container password-step">
        <transition name="slide-fade">
          <div>
            <h1>Welcome</h1>
            <div class="user-identifier">
              <div class="user-avatar">{{ email.charAt(0).toUpperCase() }}</div>
              <div class="user-email">{{ email }}</div>
            </div>
            
            <div class="form-group">
              <div class="form-control" :class="{ 'focused': isPasswordFocused || password }">
                <input 
                  type="password" 
                  id="password" 
                  v-model="password" 
                  @focus="isPasswordFocused = true" 
                  @blur="isPasswordFocused = false"
                  @keyup.enter="handleLogin"
                  placeholder=" "
                  ref="passwordInput"
                >
                <label for="password">Enter your password</label>
              </div>
              <a href="#" class="forgot-link">Forgot password?</a>
            </div>
            
            <div class="bottom-container">
              <button class="back-btn" @click="goToEmailStep">
                <span class="back-icon">‹</span> Back
              </button>
              <button class="next-btn" @click="handleLogin" @mouseover="isLoginHovered = true" @mouseleave="isLoginHovered = false" :class="{ 'hovered': isLoginHovered }">Sign in</button>
            </div>
          </div>
        </transition>
      </div>
      
      <div class="footer">
        <div>
          <select class="language-select">
            <option>English (United States)</option>
          </select>
        </div>
        <div>
          <a href="#">Help</a>
          <a href="#">Privacy</a>
          <a href="#">Terms</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      currentStep: 'email',
      email: '',
      password: '',
      isEmailFocused: false,
      isPasswordFocused: false,
      isNextHovered: false,
      isLoginHovered: false
    }
  },
  mounted() {
    // Focus email input on mount
    this.$nextTick(() => {
      this.$refs.emailInput.focus();
    });
  },
  methods: {
    goToPasswordStep() {
      if (!this.email) return;
      
      this.currentStep = 'password';
      // Focus password input after transition
      this.$nextTick(() => {
        this.$refs.passwordInput.focus();
      });
    },
    goToEmailStep() {
      this.currentStep = 'email';
      // Focus email input after transition
      this.$nextTick(() => {
        this.$refs.emailInput.focus();
      });
    },
    handleLogin() {
      if (!this.password) return;
      
      // Handle login logic here
      console.log('Logging in with:', this.email, this.password);
      // You would typically dispatch an action or call an API here
      alert(`Logged in with ${this.email}`);
    }
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Roboto', Arial, sans-serif;
}

.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f7f8f9;
}

.login-container {
  width: 100%;
  max-width: 450px;
  padding: 48px 40px 36px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  animation: fadeIn 0.5s ease-in-out;
}

.step-container {
  min-height: 320px;
}

/* Animations */
@keyframes fadeIn {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}

.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-enter-from {
  transform: translateX(20px);
  opacity: 0;
}

.logo {
  margin-bottom: 25px;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

h1 {
  font-size: 24px;
  margin-bottom: 10px;
  font-weight: 400;
  color: #202124;
}

.subtitle {
  font-size: 16px;
  margin-bottom: 30px;
  color: #5f6368;
}

.privacy-notice {
  font-size: 14px;
  margin-top: 30px;
}

.form-group {
  margin-bottom: 25px;
  text-align: left;
}

.form-control {
  position: relative;
  margin-bottom: 16px;
  transition: transform 0.3s;
}

.form-control.focused {
  transform: translateY(-3px);
}

input {
  width: 100%;
  padding: 15px;
  border: 1px solid #dadce0;
  border-radius: 4px;
  font-size: 16px;
  transition: border 0.3s;
}

input:focus {
  outline: none;
  border: 2px solid #1a73e8;
}

input:focus + label, 
input:not(:placeholder-shown) + label,
.form-control.focused label {
  transform: translateY(-24px) scale(0.75);
  color: #1a73e8;
}

label {
  position: absolute;
  left: 16px;
  top: 15px;
  color: #5f6368;
  pointer-events: none;
  transition: 0.2s ease all;
  transform-origin: left top;
}

.forgot-link {
  display: block;
  text-align: left;
  color: #1a73e8;
  text-decoration: none;
  font-weight: 500;
  font-size: 14px;
}

.bottom-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 40px;
}

.create-account {
  color: #1a73e8;
  text-decoration: none;
  font-weight: 500;
  font-size: 14px;
}

.next-btn, .back-btn {
  padding: 10px 24px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.next-btn {
  background-color: #1a73e8;
  color: white;
  animation: slideIn 0.5s ease-in-out;
}

.back-btn {
  background-color: transparent;
  color: #1a73e8;
  display: flex;
  align-items: center;
}

.back-icon {
  font-size: 18px;
  margin-right: 4px;
}

.next-btn.hovered {
  background-color: #1669d6;
  box-shadow: 0 1px 3px rgba(0,0,0,0.25);
  transform: scale(1.05);
}

@keyframes slideIn {
  0% { transform: translateX(20px); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}

/* User identifier styling for password step */
.user-identifier {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px 0 30px;
}

.user-avatar {
  width: 40px;
  height: 40px;
  background-color: #1a73e8;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  margin-right: 10px;
}

.user-email {
  font-size: 16px;
  color: #202124;
}

.footer {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
  padding: 10px;
  font-size: 12px;
  color: #5f6368;
}

.language-select {
  border: none;
  background: none;
  color: #5f6368;
}

.footer a {
  color: #5f6368;
  text-decoration: none;
  margin: 0 10px;
}

.footer a:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .login-container {
    padding: 36px 24px 24px;
    box-shadow: none;
  }
  
  .bottom-container {
    flex-direction: column;
    gap: 20px;
  }
}
</style>