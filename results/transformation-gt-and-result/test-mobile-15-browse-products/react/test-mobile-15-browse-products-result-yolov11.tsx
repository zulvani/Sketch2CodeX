import './App.css'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-0">
      <div className="mx-auto max-w-md rounded bg-white p-6 shadow">

        {/* Row 1 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-12 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping input-file */}<div obj="input-file">
                  <input
                type="file"
                className="w-full"
              />

</div>
            </div>
          </div>
        </div>

        {/* Row 2 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-12 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping image-card */}<div obj="image-card">
                  <div className="rounded w-full overflow-hidden shadow-sm">
                <div className="h-40 bg-gray-100 bg-center bg-cover flex items-center justify-center">Image</div>
                <div className="p-2 font-medium flex items-center justify-center">Title</div>
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 3 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-3 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping common-button */}<div obj="common-button">
                  <button className="w-full rounded bg-blue-500 px-4 py-2 text-white">
                Button
              </button>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-4">
            <div className="flex gap-2">
{/* Object Mapping common-button */}<div obj="common-button">
                  <button className="w-full rounded bg-blue-500 px-4 py-2 text-white">
                Button
              </button>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping common-image-button */}<div obj="common-image-button">
                  <div className="border border-red-500 p-2">
                Unknown Object
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-10">
            <div className="flex gap-2">
{/* Object Mapping common-button */}<div obj="common-button">
                  <button className="w-full rounded bg-blue-500 px-4 py-2 text-white">
                Button
              </button>

</div>
            </div>
          </div>
        </div>

        {/* Row 4 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-4 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
        </div>

        {/* Row 5 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-3 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping image-card */}<div obj="image-card">
                  <div className="rounded w-full overflow-hidden shadow-sm">
                <div className="h-40 bg-gray-100 bg-center bg-cover flex items-center justify-center">Image</div>
                <div className="p-2 font-medium flex items-center justify-center">Title</div>
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-4">
            <div className="flex gap-2">
{/* Object Mapping image-card */}<div obj="image-card">
                  <div className="rounded w-full overflow-hidden shadow-sm">
                <div className="h-40 bg-gray-100 bg-center bg-cover flex items-center justify-center">Image</div>
                <div className="p-2 font-medium flex items-center justify-center">Title</div>
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping image-card */}<div obj="image-card">
                  <div className="rounded w-full overflow-hidden shadow-sm">
                <div className="h-40 bg-gray-100 bg-center bg-cover flex items-center justify-center">Image</div>
                <div className="p-2 font-medium flex items-center justify-center">Title</div>
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-10">
            <div className="flex gap-2">
{/* Object Mapping image-card */}<div obj="image-card">
                  <div className="rounded w-full overflow-hidden shadow-sm">
                <div className="h-40 bg-gray-100 bg-center bg-cover flex items-center justify-center">Image</div>
                <div className="p-2 font-medium flex items-center justify-center">Title</div>
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 6 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-4 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-11">
            <div className="flex gap-2">
{/* Object Mapping switch */}<div obj="switch">
                  <label className="inline-flex items-center gap-2">
                <input type="checkbox" className="sr-only" />
                <span className="w-10 h-5 bg-gray-300 rounded-full"></span>
              </label>

</div>
            </div>
          </div>
        </div>

        {/* Row 7 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-6 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping image-card */}<div obj="image-card">
                  <div className="rounded w-full overflow-hidden shadow-sm">
                <div className="h-40 bg-gray-100 bg-center bg-cover flex items-center justify-center">Image</div>
                <div className="p-2 font-medium flex items-center justify-center">Title</div>
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-6 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping image-card */}<div obj="image-card">
                  <div className="rounded w-full overflow-hidden shadow-sm">
                <div className="h-40 bg-gray-100 bg-center bg-cover flex items-center justify-center">Image</div>
                <div className="p-2 font-medium flex items-center justify-center">Title</div>
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 8 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-12 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping slider */}<div obj="slider">
                  <input type="range" className="w-full" />

</div>
            </div>
          </div>
        </div>

        {/* Row 9 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-4 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping combobox */}<div obj="combobox">
                  <select className="w-full rounded border p-2">
                <option>Option 1</option>
                <option>Option 2</option>
              </select>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-5">
            <div className="flex gap-2">
{/* Object Mapping table */}<div obj="table">
                  <table className="w-full table-fixed border-collapse">
                <thead>
                  <tr>
                    <th className="border p-2 text-left">Header 1</th>
                    <th className="border p-2 text-left">Header 2</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="border p-2">Cell 1</td>
                    <td className="border p-2">Cell 2</td>
                  </tr>
                </tbody>
              </table>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-5 col-start-8">
            <div className="flex gap-2">
{/* Object Mapping time-picker */}<div obj="time-picker">
                  <input type="time" className="w-full rounded border p-2" />

</div>
            </div>
          </div>
        </div>

        {/* Row 10 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-2 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-5">
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-9">
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-11">
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  )
}
