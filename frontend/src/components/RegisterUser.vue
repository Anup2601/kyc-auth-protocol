<template>
    <div class="register-page">
      <div class="register-container">
        <div class="logo">
          <svg width="100" height="40" viewBox="0 0 100 40">
            <path d="M10,20 C10,14.5 14.5,10 20,10 H80 C85.5,10 90,14.5 90,20 V30 C90,35.5 85.5,40 80,40 H20 C14.5,40 10,35.5 10,30 V20 Z" fill="#1a73e8"/>
            <text x="50" y="28" fill="white" text-anchor="middle" font-size="14" font-weight="bold">KYC AUTH</text>
          </svg>
        </div>
        
        <!-- Registration Type Selection -->
        <div v-if="currentStep === 'selection'" class="step-container">
          <h1>Create an account</h1>
          <p class="subtitle">Choose your account type</p>
          
          <div class="account-type-selection">
            <div class="account-option" @click="selectAccountType('user')" :class="{ 'selected': accountType === 'user' }">
              <div class="option-icon">👤</div>
              <div class="option-title">Individual User</div>
              <div class="option-description">For personal account verification</div>
            </div>
            
            <div class="account-option" @click="selectAccountType('company')" :class="{ 'selected': accountType === 'company' }">
              <div class="option-icon">🏢</div>
              <div class="option-title">Company</div>
              <div class="option-description">For business verification</div>
            </div>
          </div>
          
          <div class="bottom-container">
            <a href="/" class="sign-in-link" @click="goToSignIn">Sign in instead</a>
            <button class="next-btn" @click="goToNextStep" :disabled="!accountType" :class="{ 'hovered': isNextHovered }" @mouseover="isNextHovered = true" @mouseleave="isNextHovered = false">Next</button>
          </div>
        </div>
        
        <!-- User Registration Form -->
        <div v-if="currentStep === 'user-form'" class="step-container user-form">
          <transition name="slide-fade">
            <div>
              <h1>Create your account</h1>
              <p class="subtitle">Personal information</p>
              
              <div class="form-grid">
                <div class="form-control" :class="{ 'focused': isFirstNameFocused || firstName }">
                  <input 
                    type="text" 
                    id="firstName" 
                    v-model="firstName" 
                    @focus="isFirstNameFocused = true" 
                    @blur="isFirstNameFocused = false"
                    placeholder=" "
                  >
                  <label for="firstName">First name</label>
                </div>
                
                <div class="form-control" :class="{ 'focused': isLastNameFocused || lastName }">
                  <input 
                    type="text" 
                    id="lastName" 
                    v-model="lastName" 
                    @focus="isLastNameFocused = true" 
                    @blur="isLastNameFocused = false"
                    placeholder=" "
                  >
                  <label for="lastName">Last name</label>
                </div>
              </div>
              
              <div class="form-control" :class="{ 'focused': isEmailFocused || email }">
                <input 
                  type="email" 
                  id="email" 
                  v-model="email" 
                  @focus="isEmailFocused = true" 
                  @blur="isEmailFocused = false"
                  placeholder=" "
                >
                <label for="email">Email</label>
              </div>
              
              <div class="form-grid">
                <div class="form-control" :class="{ 'focused': isPasswordFocused || password }">
                  <input 
                    :type="showPassword ? 'text' : 'password'" 
                    id="password" 
                    v-model="password" 
                    @focus="isPasswordFocused = true" 
                    @blur="isPasswordFocused = false"
                    placeholder=" "
                  >
                  <label for="password">Password</label>
                  <button type="button" class="toggle-password" @click="showPassword = !showPassword">
                    {{ showPassword ? '🙈' : '👁️' }}
                  </button>
                </div>
                
                <div class="form-control" :class="{ 'focused': isConfirmPasswordFocused || confirmPassword }">
                  <input 
                    :type="showConfirmPassword ? 'text' : 'password'" 
                    id="confirmPassword" 
                    v-model="confirmPassword" 
                    @focus="isConfirmPasswordFocused = true" 
                    @blur="isConfirmPasswordFocused = false"
                    placeholder=" "
                  >
                  <label for="confirmPassword">Confirm</label>
                  <button type="button" class="toggle-password" @click="showConfirmPassword = !showConfirmPassword">
                    {{ showConfirmPassword ? '🙈' : '👁️' }}
                  </button>
                </div>
              </div>
              
              <div class="bottom-container">
                <button class="back-btn" @click="goToSelectionStep">
                  <span class="back-icon">‹</span> Back
                </button>
                <button class="next-btn" @click="goToDocumentStep" :class="{ 'hovered': isNextHovered }" @mouseover="isNextHovered = true" @mouseleave="isNextHovered = false">Next</button>
              </div>
            </div>
          </transition>
        </div>
        
        <!-- Document Verification -->
        <div v-if="currentStep === 'document-verification'" class="step-container document-verification">
          <transition name="slide-fade">
            <div>
              <h1>Identity Verification</h1>
              <p class="subtitle">Please upload a government-issued ID</p>
              
              <div class="verification-options">
                <div class="verification-option" @click="showFileUpload = true">
                  <div class="option-icon">📁</div>
                  <div class="option-title">Upload ID</div>
                  <div class="option-description">Upload an image of your ID card or passport</div>
                </div>
                
                <div class="verification-option" @click="openCamera">
                  <div class="option-icon">📷</div>
                  <div class="option-title">Scan with Camera</div>
                  <div class="option-description">Use your camera to scan your ID</div>
                </div>
              </div>
              
              <!-- File Upload Area (hidden by default) -->
              <div v-if="showFileUpload" class="file-upload-area">
                <input 
                  type="file" 
                  id="idUpload" 
                  ref="fileInput" @change="handleFileUpload" accept="image/*" class="file-input"
                  style="display: none;"
                />

                
                <button type="button" class="browse-btn" @click="triggerFileSelect">Browse files</button>
                <div v-if="filePreview">
                 <img :src="filePreview" alt="Preview" class="id-preview" />
                </div>
              </div>
              
              <!-- Camera Capture (hidden by default) -->
              <div v-if="showCamera" class="camera-capture">
                <video ref="video" class="camera-video" autoplay></video>
                <div class="camera-controls">
                  <button class="camera-btn" @click="capturePhoto">Capture</button>
                  <button class="camera-btn cancel" @click="closeCamera">Cancel</button>
                </div>
              </div>
              
              <!-- Captured Photo (hidden by default) -->
              <div v-if="capturedImage" class="captured-image-container">
                <img :src="capturedImage" alt="Captured ID" class="captured-image">
                <div class="camera-controls">
                  <button class="camera-btn" @click="acceptImage">Accept</button>
                  <button class="camera-btn cancel" @click="retakePhoto">Retake</button>
                </div>
              </div>
              
              <div class="bottom-container">
                <button class="back-btn" @click="goToUserFormStep">
                  <span class="back-icon">‹</span> Back
                </button>
                <button class="next-btn" @click="completeRegistration" :disabled="!isDocumentUploaded" :class="{ 'hovered': isNextHovered }" @mouseover="isNextHovered = true" @mouseleave="isNextHovered = false">Complete Registration</button>
              </div>
            </div>
          </transition>
        </div>
        
        <!-- Success Message -->
        <div v-if="currentStep === 'success'" class="step-container success">
          <transition name="slide-fade">
            <div class="success-message">
              <div class="success-icon">✓</div>
              <h1>Registration Successful!</h1>
              <p>Your account has been created and is pending verification.</p>
              <p>We'll notify you via email once your identity is verified.</p>
              <button class="next-btn full-width" @click="goToSignIn">Go to Sign In</button>
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
    name: 'RegisterPage',
    data() {
      return {
        currentStep: 'selection',
        accountType: '',
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        confirmPassword: '',
        showPassword: false,
        showConfirmPassword: false,
        isFirstNameFocused: false,
        isLastNameFocused: false,
        isEmailFocused: false,
        isPasswordFocused: false,
        isConfirmPasswordFocused: false,
        isNextHovered: false,
        showFileUpload: false,
        showCamera: false,
        uploadedFile: null,
        filePreview: null,
        capturedImage: null,
        stream: null,
        isDocumentUploaded: false
      }
    },
    methods: {
      selectAccountType(type) {
        this.accountType = type;
      },
      goToNextStep() {
        if (!this.accountType) return;
        
        if (this.accountType === 'user') {
          this.currentStep = 'user-form';
        } else {
          // For company registration, we'll just show a notification for now
          alert('Company registration will be available soon!');
        }
      },
      goToSelectionStep() {
        this.currentStep = 'selection';
      },
      goToUserFormStep() {
        this.currentStep = 'user-form';
      },
      goToDocumentStep() {
        if (!this.validateUserForm()) return;
        this.currentStep = 'document-verification';
      },
      goToSignIn() {
        this.$router.push('/');
      },
      validateUserForm() {
        // Basic validation
        if (!this.firstName) {
          alert('Please enter your first name');
          return false;
        }
        if (!this.lastName) {
          alert('Please enter your last name');
          return false;
        }
        if (!this.email || !this.email.includes('@')) {
          alert('Please enter a valid email address');
          return false;
        }
        if (!this.password || this.password.length < 8) {
          alert('Password must be at least 8 characters');
          return false;
        }
        if (this.password !== this.confirmPassword) {
          alert('Passwords do not match');
          return false;
        }
        return true;
      },
      triggerFileSelect() {
        this.$refs.fileInput.click();
     },
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        this.uploadedFile = file;
        this.isDocumentUploaded = true;
        
        // Create file preview
        const reader = new FileReader();
        reader.onload = e => {
          this.filePreview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      removeFile() {
        this.uploadedFile = null;
        this.filePreview = null;
        this.isDocumentUploaded = false;
        if (this.$refs.fileInput) {
          this.$refs.fileInput.value = '';
        }
      },
      openCamera() {
        this.showFileUpload = false;
        this.showCamera = true;
        
        // Access the camera
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(stream => {
            this.stream = stream;
            this.$refs.video.srcObject = stream;
          })
          .catch(err => {
            console.error('Error accessing camera:', err);
            alert('Could not access camera. Please ensure you have granted camera permissions.');
            this.showCamera = false;
          });
      },
      closeCamera() {
        if (this.stream) {
          this.stream.getTracks().forEach(track => track.stop());
          this.stream = null;
        }
        this.showCamera = false;
      },
      capturePhoto() {
        const video = this.$refs.video;
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        this.capturedImage = canvas.toDataURL('image/png');
        this.closeCamera();
      },
      retakePhoto() {
        this.capturedImage = null;
        this.openCamera();
      },
      acceptImage() {
        this.isDocumentUploaded = true;
        this.capturedImage = this.capturedImage; 
      },
      completeRegistration() {
        if (!this.isDocumentUploaded) {
          alert('Please upload or capture a government ID document');
          return;
        }
        
        
        console.log('Registration data:', {
          accountType: this.accountType,
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          documentUploaded: !!this.uploadedFile || !!this.capturedImage
        });
        
        // Show success message
        this.currentStep = 'success';
      }
    },
    beforeUnmount() {
      // Clean up camera resources when component is destroyed
      if (this.stream) {
        this.stream.getTracks().forEach(track => track.stop());
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
  
  .register-page {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f7f8f9;
    padding: 20px;
  }
  
  .register-container {
    width: 100%;
    max-width: 500px;
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
  
  /* Account type selection */
  .account-type-selection {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
    gap: 20px;
  }
  
  .account-option {
    flex: 1;
    padding: 20px;
    border: 1px solid #dadce0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
  }
  
  .account-option:hover {
    box-shadow: 0 1px 6px rgba(0,0,0,0.1);
  }
  
  .account-option.selected {
    border-color: #1a73e8;
    box-shadow: 0 1px 6px rgba(26,115,232,0.2);
  }
  
  .option-icon {
    font-size: 32px;
    margin-bottom: 10px;
  }
  
  .option-title {
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 5px;
    color: #202124;
  }
  
  .option-description {
    font-size: 13px;
    color: #5f6368;
  }
  
  /* Form styles */
  .form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 16px;
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
  
  .toggle-password {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    cursor: pointer;
    font-size: 16px;
  }
  
  /* Verification options */
  .verification-options {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
    gap: 20px;
  }
  
  .verification-option {
    flex: 1;
    padding: 20px;
    border: 1px solid #dadce0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
  }
  
  .verification-option:hover {
    box-shadow: 0 1px 6px rgba(0,0,0,0.1);
    background-color: #f8f9fa;
  }
  
  /* File upload area */
  .file-upload-area {
    margin: 30px 0;
    border: 2px dashed #dadce0;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    transition: all 0.3s;
  }
  
  .file-upload-area:hover {
    border-color: #1a73e8;
    background-color: #f8f9fa;
  }
  
  .file-input {
    display: none;
  }
  
  .file-input-label {
    display: block;
    cursor: pointer;
    padding: 20px;
  }
  
  .upload-icon {
    font-size: 40px;
    margin-bottom: 10px;
    color: #5f6368;
  }
  
  .browse-btn {
    background-color: #1a73e8;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    margin-top: 10px;
    cursor: pointer;
  }
  
  .uploaded-file {
    padding: 10px;
  }
  
  .file-preview {
    margin-bottom: 10px;
  }
  
  .id-preview {
    max-width: 100%;
    max-height: 200px;
    border-radius: 4px;
  }
  
  .file-name {
    font-size: 14px;
    color: #202124;
    word-break: break-all;
  }
  
  .remove-file {
    background-color: #ea4335;
    color: white;
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
  }
  
  /* Camera capture */
  .camera-capture {
    margin: 30px 0;
  }
  
  .camera-video {
    width: 100%;
    max-height: 300px;
    border-radius: 8px;
    background-color: #000;
  }
  
  .camera-controls {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 15px;
  }
  
  .camera-btn {
    background-color: #1a73e8;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    cursor: pointer;
  }
  
  .camera-btn.cancel {
    background-color: #5f6368;
  }
  
  .captured-image-container {
    margin: 30px 0;
  }
  
  .captured-image {
    width: 100%;
    max-height: 300px;
    border-radius: 8px;
  }
  
  /* Success message */
  .success-message {
    padding: 30px 0;
  }
  
  .success-icon {
    width: 80px;
    height: 80px;
    background-color: #0f9d58;
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    margin: 0 auto 20px;
  }
  
  .full-width {
    width: 100%;
    margin-top: 30px;
  }
  
  /* Bottom container */
  .bottom-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 40px;
  }
  
  .sign-in-link {
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
  
  .next-btn:disabled {
    background-color: #dadce0;
    cursor: not-allowed;
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
  
  .next-btn.hovered:not(:disabled) {
    background-color: #1669d6;
    box-shadow: 0 1px 3px rgba(0,0,0,0.25);
    transform: scale(1.05);
  }
  
  @keyframes slideIn {
    0% { transform: translateX(20px); opacity: 0; }
    100% { transform: translateX(0); opacity: 1; }
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
  
  @media (max-width: 600px) {
    .register-container {
      padding: 36px 24px 24px;
      box-shadow: none;
    }
    
    .bottom-container {
      flex-direction: column;
      gap: 20px;
    }
    
    .form-grid {
      grid-template-columns: 1fr;
    }
    
    .account-type-selection, 
    .verification-options {
      flex-direction: column;
    }
  }
  </style>