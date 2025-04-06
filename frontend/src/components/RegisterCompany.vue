<template>
    <div class="register-company-container">
      <!-- Company Registration Form -->
      <div v-if="currentStep === 'company-form'" class="step-container company-form">
        <transition name="slide-fade">
          <div>
            <h1>Create company account</h1>
            <p class="subtitle">Company information</p>
            
            <!-- Profile Picture Upload -->
            <div class="profile-pic-upload">
              <div v-if="!profilePicPreview" class="profile-placeholder" @click="triggerProfilePicUpload">
                <div class="profile-icon">🏢</div>
                <div class="upload-text">Upload logo</div>
              </div>
              <div v-else class="profile-preview" @click="triggerProfilePicUpload">
                <img :src="profilePicPreview" alt="Company Logo" class="preview-image">
                <div class="overlay">Change</div>
              </div>
              <input 
                type="file" 
                ref="profilePicInput" 
                @change="handleProfilePicUpload" 
                accept="image/*" 
                class="file-input"
              >
            </div>
            
            <div class="form-control" :class="{ 'focused': isOrgNameFocused || orgName }">
              <input 
                type="text" 
                id="orgName" 
                v-model="orgName" 
                @focus="isOrgNameFocused = true" 
                @blur="isOrgNameFocused = false"
                placeholder=" "
              >
              <label for="orgName">Organization name</label>
            </div>
            
            <div class="form-grid">
              <div class="form-control" :class="{ 'focused': isGovIssueNoFocused || govIssueNo }">
                <input 
                  type="text" 
                  id="govIssueNo" 
                  v-model="govIssueNo" 
                  @focus="isGovIssueNoFocused = true" 
                  @blur="isGovIssueNoFocused = false"
                  placeholder=" "
                >
                <label for="govIssueNo">Registration number</label>
              </div>
              
              <div class="form-control" :class="{ 'focused': isPhoneFocused || phone }">
                <input 
                  type="tel" 
                  id="phone" 
                  v-model="phone" 
                  @focus="isPhoneFocused = true" 
                  @blur="isPhoneFocused = false"
                  placeholder=" "
                >
                <label for="phone">Phone number</label>
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
              <label for="email">Business email</label>
            </div>
            
            <div class="form-control" :class="{ 'focused': isAddressFocused || address }">
              <input 
                type="text" 
                id="address" 
                v-model="address" 
                @focus="isAddressFocused = true" 
                @blur="isAddressFocused = false"
                placeholder=" "
              >
              <label for="address">Business address</label>
            </div>
            
            <div class="form-grid">
              <div class="form-control" :class="{ 'focused': isCityFocused || city }">
                <input 
                  type="text" 
                  id="city" 
                  v-model="city" 
                  @focus="isCityFocused = true" 
                  @blur="isCityFocused = false"
                  placeholder=" "
                >
                <label for="city">City</label>
              </div>
              
              <div class="form-control" :class="{ 'focused': isZipCodeFocused || zipCode }">
                <input 
                  type="text" 
                  id="zipCode" 
                  v-model="zipCode" 
                  @focus="isZipCodeFocused = true" 
                  @blur="isZipCodeFocused = false"
                  placeholder=" "
                >
                <label for="zipCode">ZIP / Postal code</label>
              </div>
            </div>
            
            <div class="form-control" :class="{ 'focused': isNationalityFocused || nationality }">
              <select 
                id="nationality" 
                v-model="nationality" 
                @focus="isNationalityFocused = true" 
                @blur="isNationalityFocused = false"
                class="select-input"
              >
                <option value="" disabled selected></option>
                <option value="us">United States</option>
                <option value="uk">United Kingdom</option>
                <option value="ca">Canada</option>
                <option value="au">Australia</option>
                <option value="in">India</option>
                <option value="sg">Singapore</option>
                <!-- Add more countries as needed -->
              </select>
              <label for="nationality">Country / Region</label>
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
              <button class="next-btn" @click="goToCompanyDocumentStep" :class="{ 'hovered': isNextHovered }" @mouseover="isNextHovered = true" @mouseleave="isNextHovered = false">Next</button>
            </div>
          </div>
        </transition>
      </div>
      
      <!-- Company Document Verification -->
      <div v-if="currentStep === 'company-document-verification'" class="step-container document-verification">
        <transition name="slide-fade">
          <div>
            <h1>Business Verification</h1>
            <p class="subtitle">Please upload required verification documents</p>
            
            <div class="verification-tabs">
              <div class="tab" :class="{ 'active': activeTab === 'registration' }" @click="activeTab = 'registration'">
                Business Registration
              </div>
              <!-- <div class="tab" :class="{ 'active': activeTab === 'kyc' }" @click="activeTab = 'kyc'">
                KYC Document
              </div> -->
            </div>
            
            <!-- Registration Document Tab -->
            <div v-if="activeTab === 'registration'" class="tab-content">
              <p class="document-instruction">Upload your business registration certificate</p>
              
              <div class="verification-options">
                <div class="verification-option" @click="showRegistrationFileUpload = true">
                  <div class="option-icon">📁</div>
                  <div class="option-title">Upload Document</div>
                  <div class="option-description">Upload an image of your registration certificate</div>
                </div>
                
                <div class="verification-option" @click="openRegistrationCamera">
                  <div class="option-icon">📷</div>
                  <div class="option-title">Scan with Camera</div>
                  <div class="option-description">Use your camera to scan your document</div>
                </div>
              </div>
              
              <!-- File Upload Area (hidden by default) -->
              <div v-if="showRegistrationFileUpload" class="file-upload-area">
    <!-- Hidden File Input -->
    <input
      type="file"
      ref="registrationFileInput"
      @change="handleRegistrationFileUpload"
      accept="image/*"
      style="display: none"
    />

    <!-- Browse Button -->
    <button type="button" class="browse-btn" @click="triggerFileSelect">
      Browse files
    </button>

    <!-- Preview / File Name (optional) -->
    <div v-if="registrationFilePreview">
      <img :src="registrationFilePreview" alt="Preview" class="id-preview" />
    </div>
  </div>
              
              <!-- Camera Capture (hidden by default) -->
              <div v-if="showRegistrationCamera" class="camera-capture">
                <video ref="registrationVideo" class="camera-video" autoplay></video>
                <div class="camera-controls">
                  <button class="camera-btn" @click="captureRegistrationPhoto">Capture</button>
                  <button class="camera-btn cancel" @click="closeRegistrationCamera">Cancel</button>
                </div>
              </div>
              
              <!-- Captured Photo (hidden by default) -->
              <div v-if="capturedRegistrationImage" class="captured-image-container">
                <img :src="capturedRegistrationImage" alt="Captured Document" class="captured-image">
                <div class="camera-controls">
                  <button class="camera-btn" @click="acceptRegistrationImage">Accept</button>
                  <button class="camera-btn cancel" @click="retakeRegistrationPhoto">Retake</button>
                </div>
              </div>
            </div>
            
            
            
            <div class="bottom-container">
              <button class="back-btn" @click="goToCompanyFormStep">
                <span class="back-icon">‹</span> Back
              </button>
              <button class="next-btn" @click="completeCompanyRegistration" :disabled="!isCompanyDocumentUploaded" :class="{ 'hovered': isNextHovered }" @mouseover="isNextHovered = true" @mouseleave="isNextHovered = false">Complete Registration</button>
            </div>
          </div>
        </transition>
      </div>
      <!-- Success Message -->
      <div v-if="currentStep === 'success'" class="step-container success .register-company-container">
          <transition name="slide-fade">
            <div class="success-message">
              <div class="success-icon">✓</div>
              <h1>Registration Successful!</h1>
              <p>Your account has been created and is pending verification.</p>
              <p>We'll notify you via email once your identity is verified.</p>
              <button class="next-btn full-width" @click="goToDashboard">Go to  Dashboard</button>
            </div>
          </transition>
        </div>
    </div>
  </template>
  
  <script>
  // Add this to the existing script section
  export default {
    name: 'RegisterCompany',
    data() {
      return {
        currentStep: 'company-form',
        
        // Company form fields
        orgName: '',
        govIssueNo: '',
        phone: '',
        address: '',
        city: '',
        zipCode: '',
        nationality: '',
        
        // Company form focus states
        isOrgNameFocused: false,
        isGovIssueNoFocused: false,
        isPhoneFocused: false,
        isAddressFocused: false,
        isCityFocused: false,
        isZipCodeFocused: false,
        isNationalityFocused: false,
        
        // Company profile picture
        profilePicFile: null,
        profilePicPreview: null,
        
        // Company document verification
        activeTab: 'registration',
        
        // Registration document
        showRegistrationFileUpload: false,
        showRegistrationCamera: false,
        registrationFile: null,
        registrationFilePreview: null,
        capturedRegistrationImage: null,
        registrationStream: null,
        
        // KYC document
        showKycFileUpload: false,
        showKycCamera: false,
        kycFile: null,
        kycFilePreview: null,
        capturedKycImage: null,
        kycStream: null,
        
        isCompanyDocumentUploaded: false
      }
    },
    methods: {
      // Modify the existing methods
      goToNextStep() {
        if (!this.accountType) return;
        
        if (this.accountType === 'user') {
          this.currentStep = 'user-form';
        } else if (this.accountType === 'company') {
          this.currentStep = 'company-form';
        }
      },
      goToDashboard() {
        alert('Company Dashboard will be available soon!');
      },
      
      // Add new methods for company registration
      goToCompanyFormStep() {
        this.currentStep = 'company-form';
      },
      
      goToCompanyDocumentStep() {
        if (!this.validateCompanyForm()) return;
        this.currentStep = 'company-document-verification';
      },
      
      validateCompanyForm() {
        // Basic validation for company form
        if (!this.orgName) {
          alert('Please enter your organization name');
          return false;
        }
        if (!this.govIssueNo) {
          alert('Please enter your government issue number');
          return false;
        }
        if (!this.phone) {
          alert('Please enter your phone number');
          return false;
        }
        if (!this.email || !this.email.includes('@')) {
          alert('Please enter a valid email address');
          return false;
        }
        if (!this.address) {
          alert('Please enter your business address');
          return false;
        }
        if (!this.city) {
          alert('Please enter your city');
          return false;
        }
        if (!this.zipCode) {
          alert('Please enter your ZIP/Postal code');
          return false;
        }
        if (!this.nationality) {
          alert('Please select your country/region');
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
      
      // Profile Picture Methods
      triggerProfilePicUpload() {
        this.$refs.profilePicInput.click();
      },
      
      handleProfilePicUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        this.profilePicFile = file;
        
        // Create file preview
        const reader = new FileReader();
        reader.onload = e => {
          this.profilePicPreview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      
      // Registration Document Methods
      triggerFileSelect() {
        this.$refs.registrationFileInput.click();
     },
      handleRegistrationFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        this.registrationFile = file;
        this.isCompanyDocumentUploaded = true;
        
        // Create file preview
        const reader = new FileReader();
        reader.onload = e => {
          this.registrationFilePreview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      
      removeRegistrationFile() {
        this.registrationFile = null;
        this.registrationFilePreview = null;
        this.isCompanyDocumentUploaded = this.kycFile !== null;
        if (this.$refs.registrationFileInput) {
          this.$refs.registrationFileInput.value = '';
        }
      },
      
      openRegistrationCamera() {
        this.showRegistrationFileUpload = false;
        this.showRegistrationCamera = true;
        
        // Access the camera
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(stream => {
            this.registrationStream = stream;
            this.$refs.registrationVideo.srcObject = stream;
          })
          .catch(err => {
            console.error('Error accessing camera:', err);
            alert('Could not access camera. Please ensure you have granted camera permissions.');
            this.showRegistrationCamera = false;
          });
      },
      
      closeRegistrationCamera() {
        if (this.registrationStream) {
          this.registrationStream.getTracks().forEach(track => track.stop());
          this.registrationStream = null;
        }
        this.showRegistrationCamera = false;
      },
      
      captureRegistrationPhoto() {
        const video = this.$refs.registrationVideo;
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        this.capturedRegistrationImage = canvas.toDataURL('image/png');
        this.closeRegistrationCamera();
      },
      
      retakeRegistrationPhoto() {
        this.capturedRegistrationImage = null;
        this.openRegistrationCamera();
      },
      
      acceptRegistrationImage() {
        this.isCompanyDocumentUploaded = true;
        this.capturedRegistrationImage = this.capturedRegistrationImage; // Keep the captured image
      },
      
      // KYC Document Methods
      handleKycFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        this.kycFile = file;
        this.isCompanyDocumentUploaded = true;
        
        // Create file preview
        const reader = new FileReader();
        reader.onload = e => {
          this.kycFilePreview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      
      removeKycFile() {
        this.kycFile = null;
        this.kycFilePreview = null;
        this.isCompanyDocumentUploaded = this.registrationFile !== null;
        if (this.$refs.kycFileInput) {
          this.$refs.kycFileInput.value = '';
        }
      },
      
      openKycCamera() {
        this.showKycFileUpload = false;
        this.showKycCamera = true;
        
        // Access the camera
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(stream => {
            this.kycStream = stream;
            this.$refs.kycVideo.srcObject = stream;
          })
          .catch(err => {
            console.error('Error accessing camera:', err);
            alert('Could not access camera. Please ensure you have granted camera permissions.');
            this.showKycCamera = false;
          });
      },
      
      closeKycCamera() {
        if (this.kycStream) {
          this.kycStream.getTracks().forEach(track => track.stop());
          this.kycStream = null;
        }
        this.showKycCamera = false;
      },
      
      captureKycPhoto() {
        const video = this.$refs.kycVideo;
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        this.capturedKycImage = canvas.toDataURL('image/png');
        this.closeKycCamera();
      },
      
      retakeKycPhoto() {
        this.capturedKycImage = null;
        this.openKycCamera();
      },
      
      acceptKycImage() {
        this.isCompanyDocumentUploaded = true;
        this.capturedKycImage = this.capturedKycImage; // Keep the captured image
      },
      
      completeCompanyRegistration() {
        if (!this.isCompanyDocumentUploaded) {
          alert('Please upload at least one verification document');
          return;
        }
        
        // In a real app, you would submit the form to your backend
        console.log('Company Registration data:', {
          accountType: this.accountType,
          orgName: this.orgName,
          govIssueNo: this.govIssueNo,
          phone: this.phone,
          email: this.email,
          address: this.address,
          city: this.city,
          zipCode: this.zipCode,
          nationality: this.nationality,
          profilePicUploaded: !!this.profilePicFile,
          registrationDocUploaded: !!this.registrationFile || !!this.capturedRegistrationImage,
          kycDocUploaded: !!this.kycFile || !!this.capturedKycImage,
          kycStatus: 'pending'
        });
        
        // Show success message
        this.currentStep = 'success';
      },
      
      beforeUnmount() {
        // Clean up camera resources when component is destroyed
        if (this.stream) {
          this.stream.getTracks().forEach(track => track.stop());
        }
        if (this.registrationStream) {
          this.registrationStream.getTracks().forEach(track => track.stop());
        }
        if (this.kycStream) {
          this.kycStream.getTracks().forEach(track => track.stop());
        }
      }
    }
  }
  </script>

<style scoped>
/* Base Styles */
.register-company-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Roboto', Arial, sans-serif;
}

h1 {
  font-size: 24px;
  font-weight: 500;
  color: #202124;
  margin-bottom: 8px;
}

.subtitle {
  font-size: 16px;
  color: #5f6368;
  margin-bottom: 32px;
}

/* Form Styles */
.form-control {
  position: relative;
  margin-bottom: 24px;
}

input, select {
  width: 100%;
  padding: 12px 16px;
  font-size: 16px;
  border: 1px solid #dadce0;
  border-radius: 4px;
  outline: none;
  transition: all 0.3s;
}

input:focus, select:focus {
  border-color: #1a73e8;
  box-shadow: 0 0 0 1px #1a73e8;
}

label {
  position: absolute;
  left: 16px;
  top: 12px;
  color: #5f6368;
  font-size: 16px;
  transition: all 0.3s;
  pointer-events: none;
  transform-origin: left top;
}

.form-control.focused label {
  transform: translateY(-24px) scale(0.75);
  color: #1a73e8;
}

input:focus + label, 
input:not(:placeholder-shown) + label {
  transform: translateY(-24px) scale(0.75);
  color: #1a73e8;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

/* Button Styles */
.bottom-container {
  display: flex;
  justify-content: space-between;
  margin-top: 32px;
}

.back-btn {
  display: flex;
  align-items: center;
  background: none;
  border: none;
  color: #1a73e8;
  cursor: pointer;
  font-size: 14px;
  padding: 10px 16px;
}

.back-icon {
  margin-right: 4px;
  font-size: 18px;
}

.next-btn {
  background-color: #1a73e8;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 24px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.next-btn:hover, .next-btn.hovered {
  background-color: #0d66d0;
  box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3);
}

.next-btn:disabled {
  background-color: #dadce0;
  color: #5f6368;
  cursor: not-allowed;
}

/* Toggle Password Button */
.toggle-password {
  position: absolute;
  right: 10px;
  top: 10px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 2px;
}

/* Profile Picture Upload */
.profile-pic-upload {
  margin: 0 auto 24px;
  width: 120px;
  height: 120px;
  position: relative;
  cursor: pointer;
}

.profile-placeholder {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #f1f3f4;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 2px dashed #dadce0;
  transition: all 0.3s;
}

.profile-placeholder:hover {
  background-color: #e8f0fe;
  border-color: #1a73e8;
}

.profile-icon {
  font-size: 40px;
  margin-bottom: 5px;
  color: #5f6368;
}

.upload-text {
  font-size: 12px;
  color: #1a73e8;
}

.profile-preview {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  position: relative;
}

.preview-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
}

.profile-preview:hover .overlay {
  opacity: 1;
}

.file-input {
  display: none;
}

/* Verification Tabs */
.verification-tabs {
  display: flex;
  border-bottom: 1px solid #dadce0;
  margin-bottom: 25px;
}

.tab {
  padding: 12px 24px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 14px;
  color: #5f6368;
  position: relative;
}

.tab:hover {
  color: #1a73e8;
}

.tab.active {
  color: #1a73e8;
  font-weight: 500;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: #1a73e8;
}

.tab-content {
  padding: 20px 0;
  animation: fadeIn 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.document-instruction {
  font-size: 14px;
  color: #5f6368;
  margin-bottom: 20px;
}

/* Verification Options */
.verification-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 24px;
}

.verification-option {
  border: 1px solid #dadce0;
  border-radius: 8px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.3s;
  text-align: center;
}

.verification-option:hover {
  border-color: #1a73e8;
  background-color: #f8f9fa;
}

.option-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.option-title {
  font-weight: 500;
  margin-bottom: 8px;
}

.option-description {
  font-size: 12px;
  color: #5f6368;
}

/* File Upload Area */
.file-upload-area {
  border: 2px dashed #dadce0;
  border-radius: 8px;
  padding: 32px;
  text-align: center;
  margin-bottom: 24px;
  transition: all 0.3s;
}

.file-upload-area:hover {
  border-color: #1a73e8;
  background-color: #f8f9fa;
}

.file-input-label {
  display: block;
  cursor: pointer;
}

.upload-icon {
  font-size: 48px;
  margin-bottom: 16px;
  color: #5f6368;
}

.browse-btn {
  background-color: #1a73e8;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  margin-top: 16px;
  cursor: pointer;
}

.uploaded-file {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.file-preview {
  max-width: 100%;
  margin-bottom: 16px;
}

.id-preview {
  max-width: 300px;
  max-height: 200px;
  border-radius: 4px;
}

.file-name {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 200px;
}

.remove-file {
  background-color: #ea4335;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
}

/* Camera Capture */
.camera-capture {
  margin-bottom: 24px;
}

.camera-video {
  width: 100%;
  max-height: 400px;
  background-color: #f1f3f4;
  border-radius: 8px;
}

.camera-controls {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-top: 16px;
}

.camera-btn {
  background-color: #1a73e8;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
}

.camera-btn.cancel {
  background-color: #dadce0;
  color: #202124;
}

/* Captured Image */
.captured-image-container {
  margin-bottom: 24px;
}

.captured-image {
  max-width: 100%;
  border-radius: 8px;
}

/* Verification Status */
.verification-status {
  margin: 30px 0;
  padding: 15px;
  background-color: #fef7e0;
  border-radius: 8px;
  display: flex;
  align-items: center;
}

.status-icon {
  margin-right: 15px;
  font-size: 24px;
}

.status-text {
  font-size: 14px;
}

.pending {
  color: #f29900;
  font-weight: 500;
}

/* Transitions */
.slide-fade-enter-active, .slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter, .slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
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

/* Responsive Design */
@media (max-width: 600px) {
  .form-grid {
    grid-template-columns: 1fr;
    gap: 0;
  }
  
  .verification-options {
    grid-template-columns: 1fr;
  }
  
  .verification-tabs {
    flex-direction: row;
  }
  
  .tab {
    flex: 1;
    text-align: center;
    padding: 12px 0;
  }
  
  h1 {
    font-size: 20px;
  }
  
  .subtitle {
    font-size: 14px;
  }
}
</style>