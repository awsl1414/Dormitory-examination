<template>
    <div class="home">
        <h1>Enter Class Information</h1>
        
        <form @submit.prevent="handleSubmit">
            <div class="input-group">
                <label for="grade">Grade:</label>
                <input type="text" id="grade" v-model="grade" required />
            </div>
            <div class="input-group">
                <label for="major">Major:</label>
                <input type="text" id="major" v-model="major" required />
            </div>
            <div class="input-group">
                <label for="className">Class:</label>
                <input type="text" id="className" v-model="className" required />
            </div>
            <div class="input-group">
                <label for="dorm">Dorm:</label>
                <input type="text" id="dorm" v-model="dorm" required />
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";

export default {
    setup() {
        const grade = ref("");
        const major = ref("");
        const className = ref(""); 
        const dorm = ref("");

        const handleSubmit = async () => {
            try {
                const infoString = `${grade.value} ${major.value} ${className.value} ${dorm.value}`;
                const data = {
                    info: [infoString]
                };
                await axios.post("http://localhost:8000/class_info/create_info", data);
                alert("Data successfully sent to the server!");
            } catch (error) {
                console.error("Error sending data to the server:", error);
                alert("Failed to send data. Please try again.");
            }
        };

        return {
            grade,
            major,
            className,  
            dorm,
            handleSubmit
        };
    }
};
</script>

<!-- ... (样式部分保持不变) -->


<style scoped>
.home {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* 使用视口高度单位使.home元素占据整个屏幕高度 */
    padding: 20px;
}

h1 {
    text-align: center;
    margin-bottom: 30px;
}

form {
    width: 100%;
    max-width: 400px; /* 限制表单的最大宽度 */
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.input-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 10px;
    font-weight: 600;
}

input {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

button {
    width: 100%;
    padding: 10px 15px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #0056b3;
}
</style>