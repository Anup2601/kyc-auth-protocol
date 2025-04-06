<template>
  <div class="min-h-screen">
    <div class="heading">Dashboard</div>
    <br />
    <!-- Responsive Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <div class="card bg-blue-200 p-6 text-blue-900 shadow-lg rounded-lg">
        <span class="text-lg font-semibold">Total Users</span>
        &nbsp;&nbsp;&nbsp;
        <span class="text-3xl font-bold">{{ users.length }}</span>
      </div>
      <div class="card bg-green-200 p-6 text-green-900 shadow-lg rounded-lg">
        <span class="text-lg font-semibold">Individuals</span>
        &nbsp;&nbsp;&nbsp;
        <span class="text-3xl font-bold">{{ userStats.individual }}</span>
      </div>
      <div class="card bg-yellow-200 p-6 text-yellow-900 shadow-lg rounded-lg">
        <span class="text-lg font-semibold">Companies</span>
        &nbsp;&nbsp;&nbsp;
        <span class="text-3xl font-bold">{{ userStats.company }}</span>
      </div>
      <div class="card bg-red-200 p-6 text-red-900 shadow-lg rounded-lg">
        <span class="text-lg font-semibold">Deleted Users</span>
        &nbsp;&nbsp;&nbsp;
        <span class="text-3xl font-bold">{{ deletedUsers.length }}</span>
      </div>
    </div>

    <div class="flex flex-col md:flex-row md:items-center gap-4 mb-6">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search users..."
        class="input input-bordered w-full md:w-1/3"
      />

      <select v-model="selectedCategory" class="select select-bordered w-full md:w-1/4">
        <option value="">All Categories</option>
        <option value="individual">Individual</option>
        <option value="company">Company</option>
        <option value="verified">Verified</option>
        <option value="notVerified">Not Verified</option>
      </select>

      <select v-model="sortKey" class="select select-bordered w-full md:w-1/4">
        <option value="name">Name</option>
        <option value="email">Email</option>
        <option value="phone">Phone</option>
        <option value="country">Country</option>
        <option value="type">Type</option>
        <option value="verified">Verification</option>
      </select>

      <button @click="toggleSortOrder" class="btn btn-outline">
        Sort: {{ sortOrder === 'asc' ? 'Ascending' : 'Descending' }}
      </button>
    </div>

    <!-- Responsive Table -->
    <div class="overflow-x-auto">
      <table class="table w-full bg-white shadow rounded-lg overflow-hidden">
        <thead class="bg-blue-50 text-blue-800">
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Country</th>
            <th>Verified</th>
            <th>Type</th>
            <th v-if="isAdmin">Actions <button class="btn btn-primary mb-4" @click="openAddUserForm">  + Add User</button>    </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="user in filteredUsers"
            :key="user.id"
            class="hover:bg-blue-50 transition duration-200"
          >
            <td>
              <a href="#" @click.prevent="showDetail(user)" class="text-blue-600 hover:underline">
                {{ user.name }}
              </a>
            </td>
            <td>{{ user.email }}</td>
            <td>{{ user.phone }}</td>
            <td>{{ user.country }}</td>
            <td>{{ user.verified ? 'Yes' : 'No' }}</td>
            <td class="capitalize">{{ user.type }}</td>
            <td v-if="isAdmin">
              <button class="btn btn-sm btn-error" @click="deleteUser(user.id)">Delete</button>
              <button class="btn btn-sm btn-info ml-2" @click="editUser(user)">Edit</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Detail View Overlay -->
    <div v-if="detailUser" class="modal">
      <div class="modal-box">
        <h3 class="font-bold text-5xl">User Details</h3>
        <p><strong>Name:</strong> {{ detailUser.name }}</p>
        <p><strong>Email:</strong> {{ detailUser.email }}</p>
        <p><strong>Phone:</strong> {{ detailUser.phone }}</p>
        <p><strong>Country:</strong> {{ detailUser.country }}</p>
        <p><strong>Verified:</strong> {{ detailUser.verified ? 'Yes' : 'No' }}</p>
        <p><strong>Type:</strong> {{ detailUser.type }}</p>
        <p><strong>Documents:</strong></p>
        <ul class="list-disc ml-6">
          <li v-for="doc in detailUser.documents" :key="doc">{{ doc }}</li>
        </ul>
        <div class="modal-action">
          <button class="btn" @click="detailUser = null">Close</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Edit Modal -->
  <div v-if="editMode" class="modal">
    <div class="modal-box">
      <h3 class="font-bold text-2xl mb-4">Edit User</h3>
      <input v-model="editForm.name" class="input input-bordered w-full mb-2" placeholder="Name" />
      <input v-model="editForm.email" class="input input-bordered w-full mb-2" placeholder="Email" />
      <input v-model="editForm.phone" class="input input-bordered w-full mb-2" placeholder="Phone" />
      <input v-model="editForm.country" class="input input-bordered w-full mb-2" placeholder="Country" />
      <select v-model="editForm.type" class="select select-bordered w-full mb-2">
        <option value="individual">Individual</option>
        <option value="company">Company</option>
      </select>
      <label class="inline-flex items-center mb-4">
        <input type="checkbox" v-model="editForm.verified" class="mr-2" />
        Verified
      </label>
      <div class="modal-action">
        <button class="btn btn-success" @click="saveEdit">Save</button>
        <button class="btn btn-error" @click="cancelEdit">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [
        {
          id: 1,          name: 'Alice',          email: 'alice@example.com',          phone: '1234567890',          country: 'USA',          verified: true,          type: 'individual',
          documents: ['Passport', 'Driver’s License'],        },
        {
          id: 2,          name: 'Beta Corp',          email: 'contact@beta.com',          phone: '9876543210',          country: 'India',          verified: false,          type: 'company',
          documents: ['Business License', 'Tax ID'],        },
        {
          id: 3,          name: 'Charlie',          email: 'charlie@example.com',          phone: '2345678901',          country: 'Canada',          verified: true,          type: 'individual',
          documents: ['ID Card'],        },
        {
          id: 4,          name: 'Delta Ltd',          email: 'info@delta.com',          phone: '4567890123',          country: 'UK',          verified: false,          type: 'company',
          documents: ['Certificate of Incorporation'],        },
      ],
      deletedUsers: [],      searchQuery: '',      selectedCategory: '',      sortKey: 'name',      sortOrder: 'asc',      isAdmin: true,      editMode: false,
      editForm: {        id: null,        name: '',        email: '',        phone: '',        country: '',        verified: false,        type: '',        documents: [],      },
      detailUser: null,
    };
  },
  computed: {
    filteredUsers() {
      let filtered = this.users.filter((user) => {
        const matchesSearch =
          user.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          user.email.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          user.phone.includes(this.searchQuery) ||
          user.country.toLowerCase().includes(this.searchQuery.toLowerCase());
        const matchesCategory =
          this.selectedCategory === 'verified'
            ? user.verified
            : this.selectedCategory === 'notVerified'
            ? !user.verified
            : this.selectedCategory
            ? user.type === this.selectedCategory
            : true;
        return matchesSearch && matchesCategory;
      });

      return filtered.sort((a, b) => {
        let modifier = this.sortOrder === 'asc' ? 1 : -1;
        if (this.sortKey === 'verified') {
          return (a.verified === b.verified ? 0 : a.verified ? -1 : 1) * modifier;
        }
        return a[this.sortKey].localeCompare(b[this.sortKey]) * modifier;
      });
    },
    userStats() {
      return {
        individual: this.users.filter((u) => u.type === 'individual').length,
        company: this.users.filter((u) => u.type === 'company').length,
      };
    },
  },
  methods: {
    toggleSortOrder() {
      this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
    },
    deleteUser(id) {
      if (confirm("Are you sure you want to delete this user?")) {
        const deleted = this.users.find((user) => user.id === id);
        if (deleted) this.deletedUsers.push(deleted);
        this.users = this.users.filter((user) => user.id !== id);
      }
    },
    addUser() {
      const newUser = {
        id: this.users.length + 1,
        name: this.editForm.name,
        email: this.editForm.email,
        phone: this.editForm.phone,
        country: this.editForm.country,
        verified: this.editForm.verified,
        type: this.editForm.type,
        documents: this.editForm.documents,
      };
      this.users.push(newUser);
      this.cancelEdit();
    },
    addNewUser() {
      this.editForm = { id: null, name: '', email: '', phone: '', country: '', verified: false, type: '', documents: [] };
      this.editMode = true;
    },
    openAddUserForm() {
      this.editForm = { id: null, name: '', email: '', phone: '', country: '', verified: false, type: '', documents: [] };
      this.editMode = true;
    },
    editUser(user) {
      this.editForm = { ...user };
      this.editMode = true;
    },
    saveEdit() {
      if (this.editForm.id === null) {
        // Add new user
        const newId = this.users.length ? Math.max(...this.users.map(u => u.id)) + 1 : 1;
        const newUser = { ...this.editForm, id: newId };
        this.users.push(newUser);
      } else {
        // Edit existing user
        const index = this.users.findIndex((u) => u.id === this.editForm.id);
        if (index !== -1) {
          this.users[index] = { ...this.editForm };
        }
      }
      this.cancelEdit();
    },
    cancelEdit() {
      this.editMode = false;
      this.editForm = { id: null, name: '', email: '', phone: '', country: '', verified: false, type: '', documents: [] };
    },
    showDetail(user) {
      this.detailUser = user;
    },
  },
};
</script>

<style scoped>
@import "tailwindcss";
body {
  background-color: #5e6569; /* Light gray background */
  font-family: 'Arial', sans-serif; /* Consistent font */
}
.heading {
  font-size: 2rem;
  font-weight: bold;
  text-align: center;
  color: #2d3748; /* Darker shade for better contrast */
  margin-bottom: 0rem;
}
.flex {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
.input, .select {
  padding: 0.5rem; /* Increased for better usability */
  border-radius: 0.375rem;
  border: 1px solid #ccc;
  margin-inline: 0.3rem;
  margin-block: 0.3rem;
  transition: border-color 0.3s;
}
.input:focus, .select:focus {
  border-color: #3182ce;
}
.btn {
  padding: 0.5rem 0.5rem; /* More spacing for better click area */
  border-radius: 0.375rem;
  cursor: pointer;
  margin-top: 0.05rem;
  margin-inline: 0.2rem;
  background-color: #3182ce;
  color: white;
  transition: background-color 0.3s;
}
.btn:hover {
  background-color: #2563eb;
}
.btn-outline {
  background: none;
  border: 2px solid #3182ce;
  color: #3182ce;
}
.btn-outline:hover {
  background-color: #3182ce;
  color: white;
}
.table {
  border-collapse: collapse;
  width: 100%;
}
.table th, .table td {
  padding: 1rem; /* Larger padding for better readability */
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}
.card {
  background:#3182ce;
  color: #f0f9ff;
  height: 40px;
  align-content: center;
  font-size: 20px;
  border-radius: 0.5rem;
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1); /* Slightly stronger shadow */
  transition: transform 0.3s, box-shadow 0.3s;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}
.grid {
  gap: 1.5rem; /* Larger gap for balanced spacing */
  margin-bottom: 15px;
  text-align: center;
}
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 50;
  padding: 1rem;
}
.modal-box {
  background: white;
  padding: 2rem; /* Increased for a more comfortable layout */
  border-radius: 0.75rem; /* Smoother corners */
  max-width: 600px;
  width: 100%;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}
.modal-action {
  display: flex;
  justify-content: flex-end;
  gap: 1.5rem; /* Larger gap for clearer button separation */
  margin-top: 1.5rem;
}
.table tbody tr:hover {
  background-color: #f0f9ff;
  transition: background-color 0.3s;
}
</style>