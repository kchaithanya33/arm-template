// src/components/Common/Card.tsx
import React from 'react';

interface CardProps {
  title: string;
  children: React.ReactNode;
  className?: string;
}

export default function Card({ title, children, className = '' }: CardProps) {
  return (
    <div className={`bg-white rounded-3xl shadow-sm border border-gray-100 p-6 ${className}`}>
      {title && (
        <h3 className="text-lg font-semibold text-gray-900 mb-5">{title}</h3>
      )}
      {children}
    </div>
  );
}