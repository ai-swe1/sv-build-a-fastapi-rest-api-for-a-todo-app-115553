js
import React, { useState, useEffect } from 'react';
import { request } from './apiClient';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  useEffect(() => {
    const fetchTodos = async () => {
      const data = await request('/todos');
      setTodos(data);
    };
    fetchTodos();
  }, []);

  const handleCreateTodo = async () => {
    try {
      const data = await request('/todos', {
        method: 'POST',
        body: { title: newTodo },
      });
      setTodos([...todos, data]);
      setNewTodo('');
    } catch (err) {
      console.error(err);
    }
  };

  const handleToggleCompletion = async (id) => {
    try {
      await request(`/todos/${id}/toggle`);
      const updatedTodos = todos.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      );
      setTodos(updatedTodos);
    } catch (err) {
      console.error(err);
    }
  };

  const handleDeleteTodo = async (id) => {
    try {
      await request(`/todos/${id}`, { method: 'DELETE' });
      setTodos(todos.filter((todo) => todo.id !== id));
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h1>Todos</h1>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <input
              type='checkbox'
              checked={todo.completed}
              onChange={() => handleToggleCompletion(todo.id)}
            />
            <span>{todo.title}</span>
            <button onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <input
        type='text'
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder='New todo'
      />
      <button onClick={handleCreateTodo}>Create</button>
    </div>
  );
}
