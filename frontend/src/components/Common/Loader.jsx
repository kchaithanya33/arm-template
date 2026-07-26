// src/components/Common/Table.tsx
import React from 'react';

interface Column {
  header: string;
  accessor: string;
}

interface TableProps {
  columns: Column[];
  data: any[];
  loading?: boolean;
}

export default function Table({ columns, data, loading = false }: TableProps) {
  if (loading) {
    return <div className="text-center py-8 text-gray-500">Loading...</div>;
  }

  if (data.length === 0) {
    return <div className="text-center py-8 text-gray-500">No data found</div>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white border border-gray-200 rounded-xl">
        <thead>
          <tr className="bg-gray-50 border-b">
            {columns.map((col, i) => (
              <th key={i} className="px-6 py-4 text-left text-sm font-semibold text-gray-700">
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, rowIndex) => (
            <tr key={rowIndex} className="border-b hover:bg-gray-50">
              {columns.map((col, colIndex) => (
                <td key={colIndex} className="px-6 py-4 text-sm text-gray-700">
                  {row[col.accessor] || '-'}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}